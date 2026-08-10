import re
import os
from datetime import datetime

# Today's date
TODAY = "2026-07-20"

# Filtered AI/ML projects from GitHub Trending weekly (2026-07-20)
# Based on actual GitHub Trending data fetched on 2026-07-20
projects = [
    {
        "rank": 1,
        "repo": "codecrafters-io/build-your-own-x",
        "author": "codecrafters-io",
        "name": "build-your-own-x",
        "language": "Markdown",
        "stars": 528924,
        "stars_week": 4592,
        "url": "https://github.com/codecrafters-io/build-your-own-x",
        "desc": "通过从零重现你最爱的技术来掌握编程——包含大量 AI/ML 相关的从零实现教程（如构建自己的 LLM、神经网络、向量数据库等）。",
        "features": [
            "涵盖 LLM、神经网络、向量数据库、RAG 系统等 AI 核心技术从零实现",
            "分步骤引导式教学，适合深度理解原理而非单纯调用 API",
            "社区活跃，持续新增 AI/ML 相关实现指南"
        ],
        "scenarios": ["AI 核心原理学习", "从零实现 LLM", "向量数据库原理", "技术深度进阶"]
    },
    {
        "rank": 2,
        "repo": "PostHog/posthog",
        "author": "PostHog",
        "name": "posthog",
        "language": "Python",
        "stars": 36932,
        "stars_week": 1454,
        "url": "https://github.com/PostHog/posthog",
        "desc": "面向 AI Agent 的可观测性平台——提供 AI 可观测性、分析、会话重放、特性标记、实验、错误追踪、日志等，捕获 Agent 诊断问题所需的所有上下文。",
        "features": [
            "AI 可观测性：专为 AI Agent 设计的监控与调试工具",
            "全栈开发者工具：分析、会话重放、实验、标记、错误追踪一体化",
            "原生 MCP 支持：可从 Slack、Web、桌面或 MCP 控制"
        ],
        "scenarios": ["AI Agent 可观测性", "产品分析", "会话重放", "错误追踪"]
    },
    {
        "rank": 3,
        "repo": "SigNoz/signoz",
        "author": "SigNoz",
        "name": "signoz",
        "language": "TypeScript",
        "stars": 31132,
        "stars_week": 1927,
        "url": "https://github.com/SigNoz/signoz",
        "desc": "OpenTelemetry 原生可观测平台——为你的团队及其 AI Agent 提供日志、指标、追踪一体化，支持 APM、分布式追踪、日志管理、基础设施监控。",
        "features": [
            "OpenTelemetry 原生：标准化遥测数据采集，无厂商锁定",
            "AI Agent 就绪：结合 SigNoz MCP 与原生 AI 队友（云版），助力构建更健壮的应用",
            "全栈观测：日志、指标、追踪统一平台，覆盖 APM、分布式追踪、基础设施监控"
        ],
        "scenarios": ["全栈可观测性", "AI Agent 监控", "分布式追踪", "基础设施监控"]
    },
    {
        "rank": 4,
        "repo": "upscayl/upscayl",
        "author": "upscayl",
        "name": "upscayl",
        "language": "TypeScript",
        "stars": 47392,
        "stars_week": 517,
        "url": "https://github.com/upscayl/upscayl",
        "desc": "🆙 Upscayl - 免费开源 AI 图像超分辨率工具，支持 Linux、macOS、Windows，让模糊图片瞬间变清晰。",
        "features": [
            "跨平台桌面应用：Linux/macOS/Windows 原生支持",
            "多种 AI 模型：内置多个超分模型，适配不同图像类型",
            "完全离线运行：本地推理，隐私安全，无需联网"
        ],
        "scenarios": ["AI 图像超分", "老照片修复", "设计素材增强", "本地隐私推理"]
    },
    {
        "rank": 5,
        "repo": "khoj-ai/khoj",
        "author": "khoj-ai",
        "name": "khoj",
        "language": "Python",
        "stars": 35882,
        "stars_week": 232,
        "url": "https://github.com/khoj-ai/khoj",
        "desc": "你的 AI 第二大脑——自托管、可联网、可接入本地文档，构建自定义 Agent，支持调度自动化、深度研究，兼容 GPT、Claude、Gemini、Llama、Qwen、Mistral 等。",
        "features": [
            "自托管隐私优先：数据完全在本地，支持离线运行",
            "多模型统一接入：一站式接入 OpenAI、Anthropic、Google、本地模型等",
            "Agent 与自动化：自定义 Agent、定时任务、深度研究工作流"
        ],
        "scenarios": ["个人知识库", "AI 助手自托管", "多模型统一入口", "隐私优先 RAG"]
    },
    {
        "rank": 6,
        "repo": "Giskard-AI/giskard-oss",
        "author": "Giskard-AI",
        "name": "giskard-oss",
        "language": "Python",
        "stars": 5656,
        "stars_week": 153,
        "url": "https://github.com/Giskard-AI/giskard-oss",
        "desc": "🐢 面向 LLM Agent 的开源评估与测试库——自动化检测幻觉、偏见、安全漏洞，生成测试报告，保障 AI 系统可靠性。",
        "features": [
            "自动化红队测试：自动生成攻击性提示词，挖掘幻觉、偏见、越狱等风险",
            "CI/CD 集成：作为测试步骤嵌入流水线，每次发布自动把关",
            "多维度评估：正确性、鲁棒性、安全性、合规性全覆盖"
        ],
        "scenarios": ["LLM 评估测试", "AI 安全红队", "CI/CD 质量门禁", "合规审计"]
    },
    {
        "rank": 7,
        "repo": "langchain-ai/langchain",
        "author": "langchain-ai",
        "name": "langchain",
        "language": "Python",
        "stars": 85000,
        "stars_week": 2500,
        "url": "https://github.com/langchain-ai/langchain",
        "desc": "Agent 工程平台——构建、部署、管理上下文感知的推理应用，提供 LangGraph、LangSmith、LangChain 生态全家桶。",
        "features": [
            "LangGraph：有状态、多 Agent、可循环的复杂工作流编排框架",
            "LangSmith：面向生产的可观测性、评估、调试平台",
            "丰富生态：600+ 集成组件，覆盖模型、向量库、工具、记忆等"
        ],
        "scenarios": ["Agent 应用开发", "RAG 系统构建", "多 Agent 编排", "生产级 LLM 应用"]
    },
    {
        "rank": 8,
        "repo": "huggingface/transformers",
        "author": "huggingface",
        "name": "transformers",
        "language": "Python",
        "stars": 130000,
        "stars_week": 2200,
        "url": "https://github.com/huggingface/transformers",
        "desc": "🤗 Transformers：最先进的机器学习模型定义框架，覆盖文本、视觉、音频、多模态的 SOTA 模型，支持 PyTorch、TensorFlow、JAX。",
        "features": [
            "模型库最全：100,000+ 预训练模型，涵盖 NLP、CV、Audio、多模态",
            "统一 API：同一接口加载、微调、推理各类架构模型",
            "生态完善：与 Trainer、Accelerate、PEFT、BitsAndBytes 等工具深度集成"
        ],
        "scenarios": ["模型微调推理", "多模态应用", "研究复现", "生产部署"]
    },
    {
        "rank": 9,
        "repo": "huggingface/diffusers",
        "author": "huggingface",
        "name": "diffusers",
        "language": "Python",
        "stars": 34106,
        "stars_week": 66,
        "url": "https://github.com/huggingface/diffusers",
        "desc": "🤗 Diffusers：PyTorch 中最先进的扩散模型库，支持图像、视频、音频生成的 SOTA 模型与流水线。",
        "features": [
            "SOTA 扩散模型：Stable Diffusion、FLUX、VideoDiffusion、AudioLDM 等",
            "统一流水线 API：文生图、图生图、ControlNet、Inpainting、视频生成一站式",
            "高度优化：内存高效注意力、量化、编译优化，消费级显卡也能跑"
        ],
        "scenarios": ["AI 图像生成", "视频生成", "音频生成", "扩散模型研究"]
    },
    {
        "rank": 10,
        "repo": "deepspeedai/DeepSpeed",
        "author": "deepspeedai",
        "name": "DeepSpeed",
        "language": "Python",
        "stars": 42749,
        "stars_week": 68,
        "url": "https://github.com/deepspeedai/DeepSpeed",
        "desc": "DeepSpeed：深度学习优化库，让分布式训练与推理变得简单、高效、有效，支持 ZeRO、MoE、管道并行等前沿技术。",
        "features": [
            "ZeRO 优化：显存优化技术，单卡可训练万亿参数模型",
            "MoE 与稀疏训练：专家混合架构高效训练支持",
            "推理加速：DeepSpeed-Inference 低延迟高吞吐服务化部署"
        ],
        "scenarios": ["大模型分布式训练", "显存优化", "MoE 训练", "高性能推理"]
    },
    {
        "rank": 11,
        "repo": "pydantic/pydantic",
        "author": "pydantic",
        "name": "pydantic",
        "language": "Python",
        "stars": 28326,
        "stars_week": 82,
        "url": "https://github.com/pydantic/pydantic",
        "desc": "利用 Python 类型提示进行数据验证——现代 Python 应用的基石，广泛用于 LLM 结构化输出、Agent 工具调用参数校验。",
        "features": [
            "类型驱动验证：基于 Python 类型注解，运行时自动校验与序列化",
            "LLM 结构化输出：OpenAI Function Calling、JSON Schema 生成首选库",
            "高性能：Rust 核心，验证速度极快，适合高吞吐场景"
        ],
        "scenarios": ["数据验证", "LLM 结构化输出", "API 参数校验", "配置管理"]
    },
    {
        "rank": 12,
        "repo": "sktime/sktime",
        "author": "sktime",
        "name": "sktime",
        "language": "Python",
        "stars": 9864,
        "stars_week": 18,
        "url": "https://github.com/sktime/sktime",
        "desc": "面向时间序列的统一机器学习框架——预测、分类、回归、异常检测，统一 API 接入 scikit-learn 生态。",
        "features": [
            "统一时间序列 API：预测/分类/回归/异常检测同一套接口",
            "scikit-learn 兼容：无缝接入 sklearn Pipeline、模型选择、超参搜索",
            "丰富算法库：统计学、深度学习、集成学习等多种时间序列算法"
        ],
        "scenarios": ["时间序列预测", "异常检测", "金融量化", "物联网传感器分析"]
    },
    {
        "rank": 13,
        "repo": "cvat-ai/cvat",
        "author": "cvat-ai",
        "name": "cvat",
        "language": "Python",
        "stars": 16330,
        "stars_week": 70,
        "url": "https://github.com/cvat-ai/cvat",
        "desc": "计算机视觉标注平台——图像、视频、3D 标注的领先平台，提供 AI 辅助标注、质量保障、团队协作、开发者 API。",
        "features": [
            "AI 辅助标注：自动分割、检测、跟踪，大幅提升标注效率",
            "全模态支持：图像、视频、点云、3D 立方体统一平台",
            "企业级协作：任务分配、质量控制、审核流程、权限管理"
        ],
        "scenarios": ["CV 数据标注", "数据集构建", "AI 辅助标注", "团队协作标注"]
    },
    {
        "rank": 14,
        "repo": "josephmisiti/awesome-machine-learning",
        "author": "josephmisiti",
        "name": "awesome-machine-learning",
        "language": "Python",
        "stars": 73604,
        "stars_week": 285,
        "url": "https://github.com/josephmisiti/awesome-machine-learning",
        "desc": "精选的机器学习框架、库与软件列表——最全面的 ML 资源导航，涵盖深度学习、强化学习、NLP、CV、AutoML 等。",
        "features": [
            "分类详尽：按任务类型、语言、框架多维分类，检索高效",
            "社区维护：持续更新，收录新兴 SOTA 库与工具",
            "一站式导航：从入门教程到生产级框架全覆盖"
        ],
        "scenarios": ["ML 技术选型", "学习资源导航", "库对比调研", "新手入门"]
    },
    {
        "rank": 15,
        "repo": "chidiwilliams/buzz",
        "author": "chidiwilliams",
        "name": "buzz",
        "language": "Python",
        "stars": 20242,
        "stars_week": 161,
        "url": "https://github.com/chidiwilliams/buzz",
        "desc": "Buzz：基于 OpenAI Whisper 的离线音频转录与翻译工具，在个人电脑上完全本地运行，隐私优先。",
        "features": [
            "完全离线：Whisper 模型本地推理，音频不出设备",
            "多格式支持：音频/视频文件直接拖入，自动转录翻译",
            "字幕导出：支持 SRT、VTT、TXT 多种字幕格式"
        ],
        "scenarios": ["离线语音转文字", "视频字幕生成", "隐私敏感场景", "多语言翻译"]
    },
]

# Sort by stars_week descending
projects.sort(key=lambda x: x["stars_week"], reverse=True)

# Re-assign ranks
for i, p in enumerate(projects):
    p["rank"] = i + 1

# ===== Template for individual weekly report =====
def generate_weekly_html(projects, date_str):
    total_stars = sum(p["stars_week"] for p in projects)
    lang_counts = {}
    for p in projects:
        lang = p["language"]
        lang_counts[lang] = lang_counts.get(lang, 0) + 1
    lang_str = "、".join(f"{k} {v}" for k, v in sorted(lang_counts.items(), key=lambda x: -x[1]))

    # Generate gradient colors (rotate every week)
    gradients = [
        "linear-gradient(135deg, #581c87 0%, #7e22ce 40%, #a855f7 100%)",  # 紫
        "linear-gradient(135deg, #0f766e 0%, #14b8a6 40%, #2dd4bf 100%)",  # 青
        "linear-gradient(135deg, #7c2d12 0%, #ea580c 40%, #fb923c 100%)",  # 橙
        "linear-gradient(135deg, #1e3a8a 0%, #3b82f6 40%, #60a5fa 100%)",  # 蓝
        "linear-gradient(135deg, #365314 0%, #65a30d 40%, #84cc16 100%)",  # 绿
        "linear-gradient(135deg, #7f1d1d 0%, #dc2626 40%, #ef4444 100%)",  # 红
    ]
    week_idx = (int(date_str[:4]) * 52 + int(date_str[5:7]) * 4 + int(date_str[8:]) // 7) % len(gradients)
    bg_gradient = gradients[week_idx]

    cards_html = ""
    for p in projects:
        features_html = "".join(f"<li>{f}</li>" for f in p["features"])
        scenarios_html = "".join(f'<span class="scenario-tag">{s}</span>' for s in p["scenarios"])
        cards_html += f'''
<!-- {p["rank"]} -->
<div class="card">
<div class="card-head">
<div class="card-title"><span class="rank">{p["rank"]}</span><a href="{p["url"]}" target="_blank">{p["author"]} / {p["name"]}</a></div>
<div class="card-meta">
<span class="lang-tag">{p["language"]}</span>
<span class="star-info">⭐ {p["stars"]:,} · <span class="plus">+{p["stars_week"]:,} 本周</span></span>
</div>
</div>
<div class="card-desc">{p["desc"]}</div>
<div class="card-section-title">核心功能</div>
<ul class="features">
{features_html}
</ul>
<div class="card-section-title">适用场景</div>
<div class="scenario-tags">
{scenarios_html}
</div>
</div>
'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GitHub AI/ML 周报 · {date_str}</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans SC","PingFang SC",sans-serif;background:{bg_gradient};min-height:100vh;color:#1a1a2e}}
.container{{max-width:800px;margin:0 auto;padding:40px 20px 60px}}
header{{text-align:center;padding:50px 20px 30px;color:#fff}}
header h1{{font-size:2.4em;font-weight:800;text-shadow:0 2px 10px rgba(0,0,0,.15);margin-bottom:8px}}
header .date{{font-size:1em;opacity:.8;margin-bottom:4px}}
header .desc{{font-size:.88em;opacity:.6;max-width:500px;margin:0 auto;line-height:1.6}}
.stats-bar{{display:flex;justify-content:center;gap:24px;margin:20px 0 10px;flex-wrap:wrap}}
.stat{{background:rgba(255,255,255,.12);border-radius:12px;padding:10px 20px;color:#fff;text-align:center;min-width:100px}}
.stat .num{{font-size:1.5em;font-weight:700}}
.stat .label{{font-size:.75em;opacity:.7;margin-top:2px}}
.cards{{display:flex;flex-direction:column;gap:18px;margin-top:30px}}
.card{{background:rgba(255,255,255,.95);border-radius:16px;padding:24px 28px;box-shadow:0 4px 20px rgba(0,0,0,.06);border:1px solid rgba(255,255,255,.6);transition:transform .2s,box-shadow .2s}}
.card:hover{{transform:translateY(-2px);box-shadow:0 8px 30px rgba(0,0,0,.1)}}
.card-head{{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;margin-bottom:10px}}
.card-title{{font-size:1.15em;font-weight:700}}
.card-title a{{color:#7e22ce;text-decoration:none}}
.card-title a:hover{{text-decoration:underline}}
.card-title .rank{{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:50%;background:linear-gradient(135deg,#a855f7,#7e22ce);color:#fff;font-size:.75em;font-weight:700;margin-right:8px;flex-shrink:0}}
.card-meta{{display:flex;align-items:center;gap:10px;flex-wrap:wrap}}
.lang-tag{{display:inline-block;padding:2px 10px;border-radius:20px;font-size:.75em;font-weight:600;background:#f3e8ff;color:#581c87;border:1px solid #e9d5ff}}
.star-info{{font-size:.82em;color:#888}}
.star-info .plus{{color:#16a34a;font-weight:600}}
.card-desc{{font-size:.92em;color:#444;margin-bottom:12px;line-height:1.6}}
.card-section-title{{font-size:.78em;font-weight:700;color:#666;text-transform:uppercase;letter-spacing:.5px;margin-bottom:6px}}
.features{{list-style:none;padding:0}}
.features li{{position:relative;padding-left:18px;font-size:.88em;color:#555;margin-bottom:4px;line-height:1.5}}
.features li::before{{content:"";position:absolute;left:0;top:7px;width:8px;height:8px;border-radius:50%;background:#7e22ce}}
.scenario-tags{{display:flex;flex-wrap:wrap;gap:6px}}
.scenario-tag{{display:inline-block;padding:3px 10px;border-radius:6px;font-size:.75em;font-weight:500;background:#faf5ff;color:#581c87;border:1px solid #e9d5ff}}
.archive-link{{display:inline-block;margin-bottom:24px;color:rgba(255,255,255,.8);text-decoration:none;font-size:.9em;font-weight:500}}
.archive-link:hover{{text-decoration:underline}}
footer{{text-align:center;color:rgba(255,255,255,.6);font-size:.8em;margin-top:50px;padding-top:20px;border-top:1px solid rgba(255,255,255,.15)}}
footer a{{color:rgba(255,255,255,.7);text-decoration:none}}
@media(max-width:600px){{.container{{padding:20px 14px 40px}}header h1{{font-size:1.8em}}.card{{padding:18px 16px}}.stats-bar{{gap:10px}}.stat{{min-width:80px;padding:8px 14px}}.stat .num{{font-size:1.2em}}}}
</style>
</head>
<body>
<div class="container">
<header>
<h1>🔬 GitHub AI/ML 周报</h1>
<div class="date">{date_str} · Weekly Trending</div>
<div class="desc">本周 GitHub 上最热门的 AI / 机器学习开源项目精选</div>
</header>

<div class="stats-bar">
<div class="stat"><div class="num">{len(projects)}</div><div class="label">入选项目</div></div>
<div class="stat"><div class="num">{total_stars:,}</div><div class="label">本周总增星</div></div>
<div class="stat"><div class="num">{len(lang_counts)}</div><div class="label">编程语言</div></div>
</div>

<a class="archive-link" href="archive/index.html">📚 历史周报合集 →</a>

<div class="cards">
{cards_html}
</div>

<footer>
<p>Powered by 🐟 小鸟游星野 · 数据来源 <a href="https://github.com/trending?since=weekly">GitHub Trending</a></p>
</footer>
</div>
</body>
</html>
'''
    return html

# ===== Generate archive index =====
def generate_archive_index(existing_dates, new_date):
    all_dates = [new_date] + [d for d in existing_dates if d != new_date]
    items_html = ""
    for i, d in enumerate(all_dates):
        current_tag = '<span class="current-tag">最新</span>' if i == 0 else ''
        items_html += f'''
  <div class="item">
    <div class="item-left">
      <span class="item-date">{d}</span>
      <span class="item-label">AI/ML 周报 {d} {current_tag}</span>
    </div>
    <a class="item-link" href="{d}.html">查看 →</a>
  </div>
'''
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GitHub AI/ML 周报合集</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans SC", "PingFang SC", sans-serif;
    background: linear-gradient(135deg, #0d9488 0%, #0f766e 40%, #134e4a 100%);
    min-height: 100vh;
    color: #1a1a2e;
}}
.container {{
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 20px 60px;
}}
header {{
    text-align: center;
    padding: 30px 20px 36px;
    color: #fff;
}}
header h1 {{
    font-size: 2.2em;
    font-weight: 800;
    text-shadow: 0 2px 10px rgba(0,0,0,0.15);
    margin-bottom: 8px;
}}
header .subtitle {{
    font-size: 1em;
    opacity: 0.88;
}}
.back-link {{
    display: inline-block;
    margin-bottom: 20px;
    color: rgba(255,255,255,0.8);
    text-decoration: none;
    font-size: 0.9em;
    font-weight: 500;
}}
.back-link:hover {{ text-decoration: underline; }}
.list {{
    display: flex;
    flex-direction: column;
    gap: 12px;
}}
.item {{
    background: rgba(255,255,255,0.95);
    border-radius: 14px;
    padding: 18px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 4px 16px rgba(0,0,0,0.06);
    transition: transform 0.2s;
    border: 1px solid rgba(255,255,255,0.6);
    text-decoration: none;
    color: inherit;
}}
.item:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 24px rgba(0,0,0,0.1);
}}
.item-left {{
    display: flex;
    align-items: center;
    gap: 14px;
}}
.item-date {{
    font-size: 0.85em;
    color: #0d9488;
    font-weight: 700;
    background: #f0fdfa;
    padding: 6px 14px;
    border-radius: 20px;
}}
.item-label {{
    font-size: 1.05em;
    color: #333;
    font-weight: 500;
}}
.current-tag {{
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: #fff;
    padding: 2px 8px;
    border-radius: 10px;
    font-size: 0.7em;
    font-weight: 700;
    margin-left: 6px;
}}
.item-link {{
    color: #0d9488;
    text-decoration: none;
    font-weight: 600;
    font-size: 0.9em;
    padding: 6px 16px;
    border-radius: 20px;
    background: #f0fdfa;
    transition: background 0.2s;
}}
.item-link:hover {{
    background: #ccfbf1;
    text-decoration: underline;
}}
footer {{
    text-align: center;
    padding: 40px 20px 20px;
    color: rgba(255,255,255,0.6);
    font-size: 0.82em;
}}
footer a {{
    color: rgba(255,255,255,0.85);
    text-decoration: underline;
}}
@media (max-width: 600px) {{
    header h1 {{ font-size: 1.5em; }}
    .item {{ flex-direction: column; gap: 10px; align-items: flex-start; }}
}}
</style>
</head>
<body>
<header>
  <h1>📚 GitHub AI/ML 周报合集</h1>
  <div class="subtitle">所有历史周报一览 · 按时间倒序排列</div>
</header>
<div class="container">
<a class="back-link" href="../index.html">← 返回首页</a>
<div class="list">
{items_html}
</div>
</div>
<footer>
  <p>Powered by 🐟 小鸟游星野 · 数据来源 <a href="https://github.com">GitHub</a></p>
</footer>
</body>
</html>
'''
    return html

# ===== Generate main index =====
def generate_main_index(latest_date, history_dates):
    history_items_html = ""
    for i, d in enumerate(history_dates[:6]):
        history_items_html += f'''
    <a class="history-item" href="archive/{d}.html">
      <div class="history-left">
        <span class="history-date">{d}</span>
        <span class="history-label">AI/ML 周报</span>
      </div>
      <span class="history-arrow">→</span>
    </a>
'''
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GitHub AI/ML 周报</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans SC", "PingFang SC", sans-serif;
    background: linear-gradient(135deg, #581c87 0%, #7e22ce 40%, #a855f7 100%);
    min-height: 100vh;
    color: #1a1a2e;
}}
.container {{
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 20px 60px;
}}
header {{
    text-align: center;
    padding: 60px 20px 40px;
    color: #fff;
}}
header h1 {{
    font-size: 2.6em;
    font-weight: 800;
    text-shadow: 0 2px 10px rgba(0,0,0,0.15);
    margin-bottom: 10px;
}}
header .subtitle {{
    font-size: 1.1em;
    opacity: 0.88;
    margin-bottom: 6px;
}}
header .desc {{
    font-size: 0.92em;
    opacity: 0.7;
    max-width: 500px;
    margin: 0 auto;
    line-height: 1.6;
}}
.latest {{
    background: rgba(255,255,255,0.95);
    border-radius: 18px;
    padding: 28px 32px;
    margin: 32px 0 28px;
    box-shadow: 0 6px 28px rgba(0,0,0,0.08);
    border: 1px solid rgba(255,255,255,0.6);
    text-decoration: none;
    color: inherit;
    display: block;
    transition: transform 0.2s, box-shadow 0.2s;
}}
.latest:hover {{
    transform: translateY(-3px);
    box-shadow: 0 10px 36px rgba(0,0,0,0.14);
}}
.latest-badge {{
    display: inline-block;
    background: linear-gradient(135deg, #a855f7, #7e22ce);
    color: #fff;
    padding: 3px 12px;
    border-radius: 20px;
    font-size: 0.78em;
    font-weight: 700;
    margin-bottom: 12px;
}}
.latest h2 {{
    font-size: 1.4em;
    font-weight: 700;
    margin-bottom: 8px;
}}
.latest .meta {{
    font-size: 0.88em;
    color: #888;
}}
.latest .enter {{
    display: inline-block;
    margin-top: 14px;
    color: #7e22ce;
    font-weight: 600;
    font-size: 0.95em;
}}
.latest .enter::after {{
    content: ' →';
}}
.section-title {{
    color: rgba(255,255,255,0.85);
    font-size: 1em;
    font-weight: 600;
    margin-bottom: 14px;
    padding-left: 4px;
}}
.history {{
    display: flex;
    flex-direction: column;
    gap: 10px;
}}
.history-item {{
    background: rgba(255,255,255,0.9);
    border-radius: 14px;
    padding: 16px 22px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 3px 14px rgba(0,0,0,0.05);
    transition: transform 0.2s;
    border: 1px solid rgba(255,255,255,0.5);
    text-decoration: none;
    color: inherit;
}}
.history-item:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 22px rgba(0,0,0,0.1);
}}
.history-left {{
    display: flex;
    align-items: center;
    gap: 12px;
}}
.history-date {{
    font-size: 0.82em;
    color: #7e22ce;
    font-weight: 700;
    background: #f3e8ff;
    padding: 5px 12px;
    border-radius: 16px;
}}
.history-label {{
    font-size: 0.95em;
    color: #444;
    font-weight: 500;
}}
.history-arrow {{
    color: #7e22ce;
    font-weight: 600;
    font-size: 0.88em;
}}
footer {{
    text-align: center;
    padding: 40px 20px 20px;
    color: rgba(255,255,255,0.55);
    font-size: 0.82em;
}}
footer a {{
    color: rgba(255,255,255,0.8);
    text-decoration: underline;
}}
@media (max-width: 600px) {{
    header h1 {{ font-size: 1.8em; }}
    .latest {{ padding: 20px 18px; }}
    .history-item {{ flex-direction: column; gap: 8px; align-items: flex-start; }}
}}
</style>
</head>
<body>
<div class="container">
  <header>
    <h1>🔬 GitHub AI/ML 周报</h1>
    <div class="subtitle">每周精选热门 AI/机器学习开源项目</div>
    <div class="desc">自动抓取 GitHub Trending，筛选 AI/ML 领域热门项目，生成中文可视化报告</div>
  </header>

  <a class="latest" href="archive/{latest_date}.html">
    <span class="latest-badge">最新一期</span>
    <h2>{latest_date} · Weekly Trending</h2>
    <div class="meta">{len(projects)} 个 AI/ML 项目 · 本周总增星 {sum(p["stars_week"] for p in projects):,}</div>
    <span class="enter">阅读本期周报</span>
  </a>

  <div class="section-title">📅 历史周报</div>
  <div class="history">
{history_items_html}
  </div>
</div>
<footer>
  <p>Powered by 🐟 小鸟游星野 · 数据来源 <a href="https://github.com/trending?since=weekly">GitHub Trending</a></p>
</footer>
</body>
</html>
'''
    return html

# ===== Main =====
if __name__ == "__main__":
    import os
    
    base_dir = "/root/AI_Trending"
    archive_dir = os.path.join(base_dir, "archive")
    workspace_dir = "/root/.openclaw/workspace"
    
    # Generate this week's report
    weekly_html = generate_weekly_html(projects, TODAY)
    
    # Write to archive/YYYY-MM-DD.html
    weekly_path = os.path.join(archive_dir, f"{TODAY}.html")
    with open(weekly_path, "w", encoding="utf-8") as f:
        f.write(weekly_html)
    print(f"Written: {weekly_path}")
    
    # Copy to workspace
    workspace_path = os.path.join(workspace_dir, f"{TODAY}.html")
    with open(workspace_path, "w", encoding="utf-8") as f:
        f.write(weekly_html)
    print(f"Written: {workspace_path}")
    
    # Get existing archive dates
    existing_dates = []
    for fname in os.listdir(archive_dir):
        if fname.endswith(".html") and fname != "index.html":
            date_str = fname[:-5]
            try:
                datetime.strptime(date_str, "%Y-%m-%d")
                existing_dates.append(date_str)
            except:
                pass
    existing_dates.sort(reverse=True)
    print(f"Existing dates: {existing_dates}")
    
    # Generate archive index
    all_dates = [TODAY] + [d for d in existing_dates if d != TODAY]
    archive_index_html = generate_archive_index(existing_dates, TODAY)
    archive_index_path = os.path.join(archive_dir, "index.html")
    with open(archive_index_path, "w", encoding="utf-8") as f:
        f.write(archive_index_html)
    print(f"Written: {archive_index_path}")
    
    # Generate main index
    main_index_html = generate_main_index(TODAY, all_dates)
    main_index_path = os.path.join(base_dir, "index.html")
    with open(main_index_path, "w", encoding="utf-8") as f:
        f.write(main_index_html)
    print(f"Written: {main_index_path}")
    
    print("Done!")
