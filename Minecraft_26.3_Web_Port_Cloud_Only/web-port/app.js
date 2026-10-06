
(async () => {
  const box = document.getElementById("report");
  try {
    const r = await fetch("compatibility-report.json", {cache:"no-store"});
    const data = await r.json();
    const rows = Object.entries(data.blockers || {})
      .sort((a,b) => b[1] - a[1])
      .map(([k,v]) => `<tr><td>${k}</td><td>${v}</td><td>${data.meaning?.[k] || ""}</td></tr>`)
      .join("");
    box.innerHTML = `
      <p><strong>${data.minecraftSourceFiles}</strong> arquivos Java analisados na build do GitHub.</p>
      <table>
        <thead><tr><th>Área</th><th>Arquivos afetados</th><th>O que precisa ser portado</th></tr></thead>
        <tbody>${rows}</tbody>
      </table>`;
  } catch (e) {
    box.textContent = "Ainda não existe relatório. Rode a Action “Build Minecraft Web Port”.";
  }
})();
