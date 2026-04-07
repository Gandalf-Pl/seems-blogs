---
layout: post
title: "从「无限 buffet」到「付费墙」：AI Agent 的成本拐点已至"
date: 2026-04-07 08:00:00 +0800
categories: ai
---

周末，Anthropic 给所有 Claude Pro 用户发了一封邮件：如果你用 OpenClaw、Manis 这类 AI Agent 工具频繁调用 Claude，$20/月的「无限 buffet」已经结束了。要么走 API 按量付费，要么接受额度限制。

同一天，Bloomberg 爆出 OpenAI、Anthropic、Google 正在通过 Frontier Model Forum 共享情报，联手阻止来自中国的「对抗性蒸馏」（Adversarial Distillation）。

两条新闻看似无关，实则指向同一个拐点：**AI 算力的补贴时代正在结束，Agent 经济的真实成本开始浮出水面。**

## 一、$20 包月模式的破产

Anthropic 的通知措辞很委婉，但社区的反应很直接。

AI 产品经理 Aakash Gupta 在 X 上总结：「The $20/month all-you-can-eat buffet just closed.」

这不是 Anthropic  greedy，而是数学使然。

一个普通用户和 ChatGPT 聊一小时，可能消耗几千 token。但一个 AI Agent 要完成任务，可能需要持续调用模型数十次甚至上百次——自动浏览网页、分析代码、执行命令、总结结果。这种「agentic loop」对算力的消耗是指数级的。

Anthropic 内部信承认：「These tools put an outsized strain on our systems.」

这揭示了一个被行业长期忽视的真相：**当前 AI 应用的定价体系是建立在「人类使用」假设上的，而非「机器自主运行」。**

当 Agent 开始代替人类干活时，成本结构完全变了。

## 二、OpenClaw 之争背后的权力转移

Anthropic 新政的直接影响者之一是 OpenClaw。

这个由 Peter Steinberger 创建的开源 AI 编程代理，正是靠「接入 Claude 做复杂任务」赢得了开发者口碑。Anthropic 一边在自家产品里抄袭 OpenClaw 的功能（Claude 的 Computer Use），一边限制第三方代理的 API 访问，Steinberger 的愤怒可想而知：

「Funny how timings match up, first they copy some popular features into their closed harness, then they lock out open source.」

这场争执的本质是：**Agent 层的价值归属权。**

大模型公司想通吃——既做底层模型，又做终端 Agent。而开源社区和第三方开发者则认为，Agent 层应该是开放创新的土壤。

Anthropic 现在的策略很明确：把高频、高消耗的 Agent 场景收归自营，把低价值的聊天场景留给 $20 包月用户。

## 三、三英战吕布：AI 蒸馏的地缘政治化

如果说 Anthropic 的限制是商业层面的「成本出清」，那么 OpenAI + Anthropic + Google 的联手则是地缘政治层面的「技术封锁」。

根据 Bloomberg 报道，三家美国 AI 巨头正在共享情报，识别和阻止「对抗性蒸馏」——一种通过大量查询来复制模型能力的技术。

Anthropic 今年 2 月点名三家中国公司：DeepSeek、Moonshot（Kimi）、MiniMax，指控它们非法蒸馏 Claude。

这套叙事的核心逻辑是：**被蒸馏的模型往往会去掉原版的安全限制，构成国家安全风险。**

但更深层的焦虑或许是：中国公司正在用「蒸馏 + 算力优化」的路径，以 1/10 的成本追赶美国模型。DeepSeek-R1 的案例已经证明，通过精巧的工程优化，中小玩家也能做出接近 GPT-4o 水平的模型。

当技术领先优势不再稳固时，法律和联盟就成了新的护城河。

## 四、拐点之后：Agent 经济的三个预判

**1. 定价模型重构**

按 token 付费将让位于按「任务复杂度」或「算力时间」付费。$20 包月会成为历史，Agent 使用将进入「云资源」式的弹性计费时代。

**2. 开源模型的战略价值上升**

当商业 API 开始设限，Llama、Qwen、DeepSeek 这类可自托管的开源模型将获得更大市场份额。企业会重新权衡「 convenience vs. control」。

**3. 垂直 Agent 的分化**

通用 Agent（如 OpenClaw、Manus）将面临更严峻的商业模式考验，而垂直领域、轻量级的专用 Agent 可能找到生存空间——因为它们消耗的 token 更少，更容易在成本约束下盈利。

## 五、一句话

2025 年的春天，AI 行业正在经历从「技术展示」到「商业运营」的阵痛。当资本补贴退潮，谁能在真实的成本结构下跑通 Agent 商业模式，谁才能活到下一个周期。

Anthropic 的 $20 限制只是一个开始。
