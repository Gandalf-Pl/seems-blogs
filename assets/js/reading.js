(() => {
  const content = document.querySelector('.post-content-tech');
  if (!content) return;
  const headings = content.querySelectorAll('h2, h3');
  if (headings.length > 1) {
    headings.forEach((heading, index) => {
      if (!heading.id) heading.id = `section-${index}`;
      const item = document.createElement('li');
      if (heading.tagName === 'H3') item.className = 'toc-subheading';
      const link = document.createElement('a'); link.href = `#${encodeURIComponent(heading.id)}`; link.textContent = heading.textContent;
      item.append(link); document.getElementById('toc-list').append(item);
    });
    document.getElementById('reading-toc').hidden = false;
  }
  content.querySelectorAll('table').forEach(table => {
    const wrapper = document.createElement('div'); wrapper.className = 'table-scroll'; wrapper.tabIndex = 0; wrapper.setAttribute('role', 'region'); wrapper.setAttribute('aria-label', '文章表格，可横向滚动');
    table.before(wrapper); wrapper.append(table);
  });
})();
