(function () {
  const catalog = (window.NANO_STORIES || []).filter((story) => !story.status);
  const categories = [
    "All",
    "Biography",
    "History",
    "Ideas & Discovery",
    "Myth & Literature",
    "Science Fiction & Fantasy",
    "How Things Work",
    "Short Stories"
  ];

  const search = document.getElementById("archive-search");
  const sort = document.getElementById("archive-sort");
  const filterWrap = document.getElementById("archive-filters");
  const list = document.getElementById("archive-list");
  const resultCount = document.getElementById("result-count");
  const clearButton = document.getElementById("clear-filters");
  const emptyState = document.getElementById("empty-state");
  const emptyClear = document.getElementById("empty-clear");
  const requestedCategory = new URLSearchParams(window.location.search).get("category");

  let activeCategory = categories.includes(requestedCategory) ? requestedCategory : "All";

  filterWrap.innerHTML = categories.map((category) => `
    <button class="filter-button" type="button" data-category="${escapeHTML(category)}" aria-pressed="${category === activeCategory}">
      ${escapeHTML(category)}${category === "All" ? "" : ` <span aria-hidden="true">${countCategory(category)}</span>`}
    </button>`).join("");

  filterWrap.addEventListener("click", (event) => {
    const button = event.target.closest("[data-category]");
    if (!button) return;
    activeCategory = button.dataset.category;
    updatePressedStates();
    updateUrl();
    render();
  });

  search.addEventListener("input", render);
  sort.addEventListener("change", render);
  clearButton.addEventListener("click", clearAll);
  emptyClear.addEventListener("click", clearAll);

  render();

  function render() {
    const query = normalize(search.value);
    const filtered = catalog.filter((story) => {
      const matchesCategory = activeCategory === "All" || story.category === activeCategory;
      const haystack = normalize([story.title, story.category, story.series, story.summary, story.slug].join(" "));
      return matchesCategory && (!query || haystack.includes(query));
    });

    filtered.sort(sort.value === "title"
      ? (a, b) => a.title.localeCompare(b.title)
      : (a, b) => b.published.localeCompare(a.published));

    list.innerHTML = filtered.map((story) => {
      const date = new Intl.DateTimeFormat("en", { month: "short", year: "numeric" })
        .format(new Date(`${story.published}T12:00:00`));
      return `
        <a class="archive-row" href="${story.slug}/index.html" aria-label="Read ${escapeHTML(story.title)}">
          <span class="archive-thumb"><img src="${story.cover}" alt="" loading="lazy" /></span>
          <span class="archive-copy">
            <span class="archive-category">${escapeHTML(story.category)}</span>
            <h2>${escapeHTML(story.title)}</h2>
            <span class="archive-series">${escapeHTML(story.series)}</span>
          </span>
          <span class="archive-meta">
            <span class="archive-date">${date}</span>
            <span class="archive-arrow" aria-hidden="true">→</span>
          </span>
        </a>`;
    }).join("");

    const label = filtered.length === 1 ? "story" : "stories";
    resultCount.textContent = `${filtered.length} ${label}`;
    emptyState.hidden = filtered.length !== 0;
    list.hidden = filtered.length === 0;
    clearButton.hidden = activeCategory === "All" && !search.value;
  }

  function clearAll() {
    activeCategory = "All";
    search.value = "";
    sort.value = "newest";
    updatePressedStates();
    updateUrl();
    render();
    search.focus();
  }

  function updatePressedStates() {
    filterWrap.querySelectorAll("[data-category]").forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.category === activeCategory));
    });
  }

  function updateUrl() {
    const url = new URL(window.location.href);
    if (activeCategory === "All") url.searchParams.delete("category");
    else url.searchParams.set("category", activeCategory);
    try {
      history.replaceState({}, "", url);
    } catch (_) {
      // Some browsers restrict History API changes when this page is opened from disk.
    }
  }

  function countCategory(category) {
    return catalog.filter((story) => story.category === category).length;
  }

  function normalize(value) {
    return String(value || "")
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLocaleLowerCase();
  }

  function escapeHTML(value) {
    return String(value || "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }
})();
