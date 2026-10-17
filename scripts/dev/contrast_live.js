() => {
  // WCAG 2.x contrast of every visible text node against its effective background.
  // Text faded by opacity (its own or an ancestor's) is measured as drawn: the
  // text colour's alpha is multiplied by the cumulative opacity. Only fully
  // transparent text is skipped. Pass or fail uses the unrounded ratio.
  const parse = s => {
    const m = /rgba?\(([^)]+)\)/.exec(s || "");
    if (!m) return null;
    const p = m[1].split(/[\s,\/]+/).filter(Boolean).map(Number);
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 };
  };
  const lin = c => { c /= 255; return c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); };
  const lum = c => 0.2126 * lin(c.r) + 0.7152 * lin(c.g) + 0.0722 * lin(c.b);
  const over = (top, under) => ({
    r: top.r * top.a + under.r * (1 - top.a),
    g: top.g * top.a + under.g * (1 - top.a),
    b: top.b * top.a + under.b * (1 - top.a), a: 1 });
  const background = el => {
    const layers = [];
    for (let e = el; e; e = e.parentElement) {
      const c = parse(getComputedStyle(e).backgroundColor);
      if (c && c.a > 0) { layers.push(c); if (c.a >= 1) break; }
    }
    let base = parse(getComputedStyle(document.body).backgroundColor) || { r: 255, g: 255, b: 255, a: 1 };
    if (base.a < 1) base = over(base, { r: 255, g: 255, b: 255, a: 1 });
    for (let i = layers.length - 1; i >= 0; i--) base = over(layers[i], base);
    return base;
  };
  const opacityOf = el => {
    let opacity = 1;
    for (let e = el; e; e = e.parentElement) opacity *= parseFloat(getComputedStyle(e).opacity);
    return opacity;
  };
  const shown = el => {
    const r = el.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) return false;
    for (let e = el; e; e = e.parentElement) {
      const cs = getComputedStyle(e);
      if (cs.visibility === "hidden" || cs.display === "none") return false;
    }
    return opacityOf(el) > 0;
  };
  const measure = (el, colour, text) => {
    const cs = getComputedStyle(el);
    const bg = background(el);
    const c = parse(colour);
    const fg = over({ ...c, a: c.a * opacityOf(el) }, bg);
    const l1 = lum(fg), l2 = lum(bg);
    const ratio = (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
    const size = parseFloat(cs.fontSize), weight = parseInt(cs.fontWeight, 10);
    const large = size >= 24 || (size >= 18.66 && weight >= 700);
    return { text: text.slice(0, 48), exact: ratio, ratio: Math.round(ratio * 100) / 100,
             need: large ? 3 : 4.5, colour, opacity: Math.round(opacityOf(el) * 1000) / 1000,
             background: `rgb(${Math.round(bg.r)}, ${Math.round(bg.g)}, ${Math.round(bg.b)})`,
             element: el.tagName.toLowerCase() + (el.className && typeof el.className === "string"
               ? "." + el.className.trim().split(/\s+/).join(".") : "") };
  };
  const seen = new Set(), all = [];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (walker.nextNode()) {
    const node = walker.currentNode, el = node.parentElement;
    if (!el || seen.has(el) || !node.textContent.trim()) continue;
    if (el.closest("script, style, noscript")) continue;
    seen.add(el);
    if (shown(el)) all.push(measure(el, getComputedStyle(el).color, node.textContent.trim()));
  }
  for (const input of document.querySelectorAll("input[placeholder]")) {
    if (shown(input) && !input.value)
      all.push(measure(input, getComputedStyle(input, "::placeholder").color, "placeholder: " + input.placeholder));
  }
  const failures = all.filter(x => x.exact < x.need).map(({ exact, ...rest }) => rest);
  return { sampled: all.length, failures };
}
