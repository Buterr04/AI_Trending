import re
from datetime import datetime

# This week's data (Monday July 13, 2026)
TODAY = "2026-07-13"

# Filtered AI/ML projects from GitHub Trending weekly
projects = [
    {
        "rank": 1,
        "repo": "TencentCloud/CubeSandbox",
        "author": "TencentCloud",
        "name": "CubeSandbox",
        "language": "Rust",
        "stars": 9803,
        "stars_week": 7440,
        "url": "https://github.com/TencentCloud/CubeSandbox",
        "desc": "Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.",
        "features": [
            "即时启动：毫秒级沙箱冷启动，支持高并发 AI Agent 隔离运行",
            "安全隔离：基于 Rust 编写，内存安全，防止代码逃逸与资源滥用",
            "轻量级设计：极低资源占用，适合大规模 AI Agent 编排部署"
        ],
        "scenarios": ["AI Agent 运行环境", "代码执行沙箱", "多租户隔离", "云原生部署"]
    },
    {
        "rank": 2,
        "repo": "ogulcancelik/herdr",
        "author": "ogulcancelik",
        "name": "herdr",
        "language": "Rust",
        "stars": 15791,
        "stars_week": 3928,
        "url": "https://github.com/ogulcancelik/herdr",
        "desc": "终端里的 Agent 多路复用器——在一个终端会话中同时管理和调度多个 AI Agent，像 tmux 管理 shell 一样管理 Agent。",
        "features": [
            "多 Agent 并发管理：单终端同时运行和切换多个 AI Agent 会话",
            "灵活路由分发：根据任务类型自动分配到最合适的 Agent",
            "轻量终端原生：纯 CLI 设计，无需 GUI，远程服务器也能用"
        ],
        "scenarios": ["多 Agent 开发", "终端工作流", "AI Agent 编排", "DevOps 自动化"]
    },
    {
        "rank": 3,
        "repo": "diegosouzapw/OmniRoute",
        "author": "diegosouzapw",
        "name": "OmniRoute",
        "language": "TypeScript",
        "stars": 16228,
        "stars_week": 4506,
        "url": "https://github.com/diegosouzapw/OmniRoute",
        "desc": "永不停机的 AI Gateway——一个端点接入 231+ 供应商（50+ 免费），自动路由、负载均衡、故障切换，编码永不中断。",
        "features": [
            "231+ 供应商聚合：一个 API 端点访问所有主流 LLM 供应商，50+ 免费额度",
            "智能路由与故障切换：自动选择最优供应商，单点故障不影响服务",
            "零配置负载均衡：开箱即用的流量分配，最大化利用免费额度"
        ],
        "scenarios": ["API 网关", "LLM 成本优化", "多模型调度", "高可用部署"]
    },
    {
        "rank": 4,
        "repo": "stablyai/orca",
        "author": "stablyai",
        "name": "orca",
        "language": "TypeScript",
        "stars": 16992,
        "stars_week": 4481,
        "url": "https://github.com/stablyai/orca",
        "desc": "Agent 集群开发环境——并行运行多个编码 Agent，统一管理和监控，像 IDE 一样开发 Agent 集群。",
        "features": [
            "并行 Agent 运行：同时启动和管理多个编码 Agent 实例",
            "统一开发环境：Agent IDE (ADE) 提供代码编辑、调试、监控一体化体验",
            "灵活调度：支持任意编码 Agent 框架，不锁定特定实现"
        ],
        "scenarios": ["Agent 开发", "多 Agent 集群", "AI 编程", "开发工具"]
    },
    {
        "rank": 5,
        "repo": "bradautomates/claude-video",
        "author": "bradautomates",
        "name": "claude-video",
        "language": "Python",
        "stars": 12268,
        "stars_week": 7155,
        "url": "https://github.com/bradautomates/claude-video",
        "desc": "给 Claude 看视频的能力——/watch 下载、抽帧、转录，全部交给 Claude 处理。",
        "features": [
            "视频下载与抽帧：自动下载视频并提取关键帧供模型理解",
            "语音转录集成：自动生成字幕文本，配合视觉信息多模态理解",
            "Claude 原生集成：通过 slash command 无缝融入 Claude Code 工作流"
        ],
        "scenarios": ["视频内容理解", "多模态 AI", "教育培训", "媒体分析"]
    },
    {
        "rank": 6,
        "repo": "alibaba/page-agent",
        "author": "alibaba",
        "name": "page-agent",
        "language": "TypeScript",
        "stars": 24433,
        "stars_week": 4353,
        "url": "https://github.com/alibaba/page-agent",
        "desc": "阿里开源的网页 GUI Agent——用自然语言操控网页界面，自动执行点击、填写、导航等交互操作。",
        "features": [
            "自然语言操控：用日常语言描述操作意图，Agent 自动执行网页交互",
            "全链路 UI 自动化：覆盖表单填写、按钮点击、页面导航等常见操作",
            "轻量集成：JavaScript 嵌入即用，无需额外运行时"
        ],
        "scenarios": ["Web 自动化", "RPA", "UI 测试", "数据采集"]
    },
    {
        "rank": 7,
        "repo": "alirezarezvani/claude-skills",
        "author": "alirezarezvani",
        "name": "claude-skills",
        "language": "Python",
        "stars": 8921,
        "stars_week": 6978,
        "url": "https://github.com/alirezarezvani/claude-skills",
        "desc": "Claude 技能库——为 Claude Code 提供可复用、可组合的技能模块，扩展编程助手能力边界。",
        "features": [
            "技能模块化：将常用工作流封装为可复用的 Skill，一键调用",
            "社区驱动生态：大量第三方 Skill 可直接安装，持续扩展能力边界",
            "组合式工作流：多个 Skill 自由编排，构建复杂自动化流水线"
        ],
        "scenarios": ["AI 编程助手", "工作流自动化", "技能复用", "开发者效率"]
    },
    {
        "rank": 8,
        "repo": "openai/codex-plugin-cc",
        "author": "openai",
        "name": "codex-plugin-cc",
        "language": "JavaScript",
        "stars": 26016,
        "stars_week": 4143,
        "url": "https://github.com/openai/codex-plugin-cc",
        "desc": "在 Claude Code 中调用 Codex——让 Claude Code 用户直接使用 OpenAI Codex 能力进行代码审查和任务委派，两大生态互联互通。",
        "features": [
            "Claude Code 内置 Codex：无需切换工具，在 Claude Code 中直接调用 Codex",
            "代码审查增强：利用 Codex 的代码理解能力辅助 Review",
            "任务智能委派：根据任务类型自动选择 Claude 或 Codex 执行"
        ],
        "scenarios": ["AI 编程", "代码审查", "多模型协作", "开发者工具"]
    },
    {
        "rank": 9,
        "repo": "JuliusBrussee/caveman",
        "author": "JuliusBrussee",
        "name": "caveman",
        "language": "JavaScript",
        "stars": 85432,
        "stars_week": 1180,
        "url": "https://github.com/JuliusBrussee/caveman",
        "desc": "Claude Code 效率神器——通过精简提示词和上下文策略，将代码生成 token 消耗削减 65%，省时省钱。",
        "features": [
            "Token 大幅削减：优化提示词策略，减少 65% 的 LLM token 消耗",
            "即插即用：作为 Claude Code skill 直接加载，无需额外配置",
            "智能上下文压缩：自动识别冗余信息，保留核心语义"
        ],
        "scenarios": ["Claude Code 用户", "成本优化", "大型项目开发", "提示词工程"]
    },
    {
        "rank": 10,
        "repo": "usestrix/strix",
        "author": "usestrix",
        "name": "strix",
        "language": "Python",
        "stars": 37705,
        "stars_week": 2666,
        "url": "https://github.com/usestrix/strix",
        "desc": "开源 AI 渗透测试工具——自动发现并修复应用安全漏洞，让安全测试像写代码一样简单。",
        "features": [
            "AI 驱动漏洞扫描：基于 LLM 智能分析攻击面，自动生成测试用例",
            "全自动修复建议：发现漏洞后提供可执行的修复代码和详细解释",
            "多协议支持：覆盖 HTTP/WebSocket/API 等常见攻击向量"
        ],
        "scenarios": ["安全测试", "渗透测试", "DevSecOps", "代码审计"]
    },
    {
        "rank": 11,
        "repo": "Zackriya-Solutions/meetily",
        "author": "Zackriya-Solutions",
        "name": "meetily",
        "language": "Rust",
        "stars": 18353,
        "stars_week": 1993,
        "url": "https://github.com/Zackriya-Solutions/meetily",
        "desc": "隐私优先的 AI 会议助手——4 倍速 Parakeet/Whisper 实时转写，本地运行，会议内容不出设备。",
        "features": [
            "本地实时转写：基于 Parakeet/Whisper 的 4 倍速语音转文字，数据不离设备",
            "隐私优先架构：所有处理在本地完成，零数据上传云端",
            "AI 会议摘要：自动生成会议纪要、行动项和关键决策提取"
        ],
        "scenarios": ["会议记录", "隐私合规", "语音转文字", "远程办公"]
    },
    {
        "rank": 12,
        "repo": "wonderwhy-er/DesktopCommanderMCP",
        "author": "wonderwhy-er",
        "name": "DesktopCommanderMCP",
        "language": "TypeScript",
        "stars": 5421,
        "stars_week": 872,
        "url": "https://github.com/wonderwhy-er/DesktopCommanderMCP",
        "desc": "桌面级 MCP 服务器——让 AI 直接操控桌面应用、文件系统、Shell，实现真正的计算机使用自动化。",
        "features": [
            "桌面全权控制：文件操作、应用启动、剪贴板、窗口管理一站式覆盖",
            "MCP 标准协议：兼容所有支持 MCP 的 AI 客户端（Claude、Cursor 等）",
            "安全沙箱模式：可配置权限边界，防止误操作敏感资源"
        ],
        "scenarios": ["桌面自动化", "MCP 生态", "AI 操作电脑", "效率工具"]
    },
    {
        "repo": "vxcontrol/pentagi",
        "author": "vxcontrol",
        "name": "pentagi",
        "language": "Go",
        "stars": 12519,
        "stars_week": 3763,
        "url": "https://github.com/vxcontrol/pentagi",
        "desc": "自主渗透测试 Agent 系统——多 Agent 协作完成从信息收集到漏洞利用的全流程渗透测试。",
        "features": [
            "多 Agent 协作：侦察、扫描、利用、后渗透各阶段由专用 Agent 执行",
            "自主决策链：Agent 根据上下文自动规划下一步动作，无需人工干预",
            "完整渗透流程：覆盖外网渗透、内网横向、权限提升、痕迹清理全链路"
        ],
        "scenarios": ["自动化渗透测试", "红队演练", "安全评估", "Agent 编排"]
    },
    {
        "repo": "ruvnet/RuView",
        "author": "ruvnet",
        "name": "RuView",
        "language": "Rust",
        "stars": 8523,
        "stars_week": 3992,
        "url": "https://github.com/ruvnet/RuView",
        "desc": "高性能代码可视化工具——将代码库渲染为交互式图谱，支持依赖分析、调用链追踪、架构洞察。",
        "features": [
            "交互式代码图谱：函数调用、模块依赖、数据流向可视化呈现",
            "增量更新渲染：大型代码库毫秒级刷新，支持实时编辑同步",
            "多语言统一视图：Rust/JS/Python/Go 等混合项目统一建模分析"
        ],
        "scenarios": ["代码审查", "架构分析", "遗留系统重构", "团队知识传递"]
    },
    {
        "repo": "ChromeDevTools/chrome-devtools-mcp",
        "author": "ChromeDevTools",
        "name": "chrome-devtools-mcp",
        "language": "TypeScript",
        "stars": 46021,
        "stars_week": 2272,
        "url": "https://github.com/ChromeDevTools/chrome-devtools-mcp",
        "desc": "Chrome DevTools MCP 服务器——让编码 Agent 直接操控 Chrome DevTools，实时调试、性能分析和 DOM 操作。",
        "features": [
            "Agent 原生调试：AI 编码助手通过 MCP 协议直接操控浏览器开发者工具",
            "实时性能分析：自动检测页面性能瓶颈并给出优化建议",
            "DOM 实时操作：Agent 可直接审查和修改页面元素与样式"
        ],
        "scenarios": ["AI 辅助调试", "性能优化", "前端自动化", "开发工具"]
    },
    {
        "repo": "tt-a1i/archify",
        "author": "tt-a1i",
        "name": "archify",
        "language": "TypeScript",
        "stars": 6234,
        "stars_week": 2397,
        "url": "https://github.com/tt-a1i/archify",
        "desc": "Any Agent Skill：生成美观架构图的技能模块，支持深/浅色主题切换和 PNG/JPEG/WebP/SVG 导出。",
        "features": [
            "一键生成架构图：Agent 调用即可生成专业级架构图表",
            "主题自适应：内置深/浅色主题，自动适配文档风格",
            "多格式导出：支持 PNG/JPEG/WebP/SVG，满足文档与演示需求"
        ],
        "scenarios": ["架构设计", "技术文档", "Agent 技能", "图表生成"]
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
    # existing_dates is a list of date strings in descending order
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
    # history_dates already includes latest_date at position 0
    history_items_html = ""
    for i, d in enumerate(history_dates[:6]):  # show first 6
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
