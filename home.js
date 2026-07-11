(function () {
  const catalog = (window.NANO_STORIES || []).filter((story) => !story.status);
  const latest = [...catalog]
    .sort((a, b) => b.published.localeCompare(a.published))
    .slice(0, 12);

  const grid = document.getElementById("latest-grid");
  const total = document.getElementById("story-total");

  if (total) total.textContent = String(catalog.length);
  if (!grid) return;

  grid.innerHTML = latest.map((story, index) => {
    const date = new Intl.DateTimeFormat("en", { month: "short", day: "numeric" })
      .format(new Date(`${story.published}T12:00:00`));
    const imagePriority = index < 3 ? 'loading="eager" fetchpriority="high"' : 'loading="lazy"';

    return `
      <a class="story-card" href="${story.slug}/index.html" aria-label="Read ${escapeHTML(story.title)}">
        <div class="story-cover">
          <img src="${story.cover}" alt="" ${imagePriority} />
          <span class="new-badge">New · ${date}</span>
        </div>
        <div class="story-body">
          <p class="story-kicker">${escapeHTML(story.category)}</p>
          <h3 class="story-title">${escapeHTML(story.title)}</h3>
          <p class="story-summary">${escapeHTML(story.summary || story.series)}</p>
          <span class="story-action"><span>Start reading</span><span aria-hidden="true">→</span></span>
        </div>
      </a>`;
  }).join("");

  function escapeHTML(value) {
    return String(value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }
})();
