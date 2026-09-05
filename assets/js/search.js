(() => {
  const source = document.getElementById('post-data');
  if (!source) return;
  const posts = JSON.parse(source.textContent);
  const input = document.getElementById('post-search');
  const buttons = Array.from(document.querySelectorAll('[data-topic]'));
  const patterns = {agent: /agent|智能体|智能代理|openclaw|miclaw/i, models: /模型|开源|参数|推理|deepseek|gpt|gemini|claude|moe/i, practice: /实测|评测|实践|指南|产品|工具|编程|coding|工作流|应用|落地|部署/i, industry: /产业|行业|资本|融资|经济|成本|商业|安全|治理|监管|合规|主权|算力/i};
  let topic = 'all';
  function render() {
    const query = input.value.trim().toLocaleLowerCase();
    const active = Boolean(query) || topic !== 'all';
    document.getElementById('default-posts').hidden = active;
    document.getElementById('search-results').hidden = !active;
    if (!active) return;
    const matches = posts.filter(post => post.title.toLocaleLowerCase().includes(query) && (topic === 'all' || patterns[topic].test(post.title)));
    const fragment = document.createDocumentFragment();
    for (const post of matches) {
      const link = document.createElement('a'); link.className = 'post-card'; link.href = post.url;
      const title = document.createElement('h3'); title.textContent = post.title;
      const meta = document.createElement('div'); meta.className = 'card-meta';
      const date = document.createElement('time'); date.dateTime = post.date; date.textContent = post.date;
      const category = document.createElement('span'); category.textContent = post.category;
      meta.append(date, category); link.append(title, meta); fragment.append(link);
    }
    document.getElementById('result-list').replaceChildren(fragment);
    document.getElementById('result-count').textContent = `找到 ${matches.length} 篇文章`;
    document.getElementById('empty-results').hidden = matches.length > 0;
  }
  input.addEventListener('input', render);
  buttons.forEach(button => button.addEventListener('click', () => {
    topic = button.dataset.topic;
    buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    render();
  }));
  document.getElementById('search-tools').hidden = false;
})();
