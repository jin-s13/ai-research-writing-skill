# *ACL 论文集排版说明

以下说明适用于：向 ACL 会议提交审稿的论文（下称「审稿版」），以及录用后收入论文集的论文（下称「终稿版」）。所有作者均须遵守这些规范。

## 样式文件

*ACL 提供满足上述要求的 LaTeX 与 Microsoft Word 样式文件，获取地址：

> https://acl-org.github.io/ACLPUB/

我们强烈建议使用这些已针对 *ACL 论文集定制的样式文件。

## 篇幅

会议接受长文与短文投稿。

- 长文审稿版：正文最多八（8）页，参考文献页数不限。
- 长文录用后终稿：正文可多一页，共九（9）页，致谢与参考文献页数不限，以便纳入审稿意见。
- 短文审稿版：正文最多四（4）页，参考文献页数不限。
- 短文终稿：正文最多五（5）页，致谢与参考文献页数不限。

无论长文或短文，属于正文的全部图表须落在上述页数限制内。

会议鼓励提交附录与补充材料，它们不必计入上述页数。但审稿版须能独立阅读：审稿人是否查看附录或补充材料为可选项。详见 [附录](#附录) 与 [补充材料](#补充材料)。

审稿版不得引用审稿人无法获取的文档、代码或数据资源以获取进一步细节。

不符合上述要求的论文可能不经审稿即被拒。

各 workshop 主席可对篇幅及是否欢迎附录/补充材料另有规定；始终以相应征稿说明（call for papers）为准。

## 匿名

审稿为双盲，审稿版不得包含任何可识别作者身份的信息（如姓名、单位、URL）。

须避免暴露作者身份的自引，例如：

> We previously showed (Gusfield, 1997)...

也应避免匿名引用，例如：

> We previously showed (Anonymous, 1997)...

应改用如下形式：

> Gusfield (1997) previously showed...

审稿版不得包含致谢。

**不符合上述要求的论文可能不经审稿即被拒。**

已投稿论文的任何非存档预印版本应在 START 投稿表单中列出，但不得出现在审稿版正文中。审稿人通常知晓作者可能在其他场合报告预印工作，但不会从投稿表单获知既往报告列表。

论文录用后，终稿可包含作者姓名与单位，并允许使用自引。

## 一稿多投

已投稿或拟投稿至其他会议/期刊的论文，须在 START 投稿表单中说明，若被 *ACL 录用须从其他场合撤回。

被 *ACL 录用展示的论文，作者须在终稿（camera-ready）截止前通知程序主席是否到会报告。我们不会发表或展示与已在别处（或将要）发表之论文在内容或结果上显著重叠的稿件。

向 *ACL 提交多篇论文时，须确保各稿在内容或结果上的重叠不超过 25%。

## 排版细则

### 文件格式

论文须为 Adobe 便携式文档格式（PDF）。

请确保 PDF 嵌入全部必要字体（尤其树状图、符号及亚洲语言）。打印或生成 PDF 时，打印机设置中通常可选择不嵌入、嵌入全部或仅嵌入非标准字体；请选择嵌入**全部**字体。

**发送前，请在不同于创作环境的计算机上打印测试 PDF。**

部分文字处理软件会生成体积很大的 PDF，每页被渲染为图像，打印效果可能很差。此时请尝试其他方式生成 PDF。

所有论文必须使用 **A4 纸张**（21 cm × 29.7 cm），不得使用其他纸张尺寸。

若无法满足上述要求，请尽快联系出版主席。

### 版式

除页码外，全部文字须落在页边距内。

审稿版应有页码，居中于页脚；**终稿版不得编页码。**

正文须为双栏排版。例外：标题、作者姓名与完整地址须居中置于首页顶部；全宽图、表亦可跨双栏。

A4 页面精确尺寸如下：

* 左边距：2.5 cm
* 右边距：2.5 cm
* 上边距：2.5 cm
* 下边距：2.5 cm
* 栏宽：7.7 cm
* 栏高：24.7 cm
* 栏间距：0.6 cm

审稿版应打印标尺（文章左右边距的行号），便于审稿人针对具体行评论。标尺不得改变页面其他内容的版式。终稿不得含标尺。

### 字体

除非拉丁文字与数学公式外，正文应使用 **Times Roman**。若不可用，可使用 **Times New Roman** 或 **Computer Modern Roman**。

下表规定各类文字的字号与样式：

| 文字类型          | 字号 | 样式 |
| --------------------- | --------- | ----- |
| paper title           | 15 pt     | bold  |
| author names          | 12 pt     | bold  |
| author affiliation    | 12 pt     |       |
| the word ``Abstract'' | 12 pt     | bold  |
| section titles        | 12 pt     | bold  |
| subsection titles     | 11 pt     | bold  |
| document text         | 11 pt     |       |
| captions              | 10 pt     |       |
| abstract text         | 10 pt     |       |
| bibliography          | 10 pt     |       |
| footnotes             | 9 pt      |       |

### 标题与作者

标题、作者姓名与单位信息应跨双栏居中。

标题以 15 pt 粗体居中置于首页顶部。过长标题可排成两行，中间不留空行。标题距页顶 2.5 cm。标题使用 [title case](https://apastyle.apa.org/style-grammar-guidelines/capitalization/title-case)；除缩写（如 “BLEU”）或通常大写的专有名词（如 “English”）外，勿全部大写。

作者姓名与单位置于标题下方。写全名；勿将名缩写为首字母，除非通常即以首字母书写（写 “Margaret Mitchell”，勿写 “M. Mitchell”）。姓氏勿全大写（写 “Mitchell”，勿写 “MITCHELL”）。

单位信息勿用脚注。单位应含作者完整地址，并尽可能提供电子邮箱。

标题、作者与地址须与投稿网站填写信息完全一致，以保持会议各出版物作者信息一致。若不一致，出版主席可能在不咨询作者的情况下自行更正；请务必自行核对。

正文从首页距顶 7.5 cm 处开始。**即使审稿版也须为终稿中的姓名与地址预留空间。**

### 摘要

摘要排在第一栏开头。在摘要正文上方以 12 pt 粗体居中排 **Abstract**。摘要宽度较正常栏宽每侧各窄 0.6 cm。摘要正文为 10 pt roman、单倍行距。

摘要应简洁概括论文主旨与结论，不超过 200 词。

### 正文

摘要之后立即开始双栏正文，11 pt roman、单倍行距。

新段首行缩进 0.4 cm，章节首段除外。

### 章节

使用阿拉伯数字编号章节，便于交叉引用。小节编号为「节号.小节号」，例如：

> 1 Introduction

或

> 6.1 File Format

### 脚注

脚注置于页底，9 pt 字号。可编号，或以星号等符号标注。脚注与正文之间应有分隔线。

### 图与表

尽可能将图、表放在首次讨论处附近，而非一律置于文末。过宽图/表可跨双栏。

为照顾色觉障碍读者及黑白打印，强烈建议保证灰度可读。不禁止彩色，但勿仅靠颜色区分关键信息。

**图题/表题：** 每个图/表须有题注，并按顺序编号，例如：

> Figure 1: Caption of the Figure.

以及

> Table 1: Caption of the Table.

题注置于图/表下方，10 pt roman。单行题注居中；多行题注左对齐。

### 超链接

文内与文外超链接应为深蓝色（hex #000099），无下划线、无边框。

### 非英文文字

非英文正文应附英文翻译；非拉丁文字还应附拉丁转写，因并非所有读者都能轻松辨认非拉丁字符。

例如，παράδειγμα *paradeigma* ‘example’ 为希腊词，以下为希腊例句：

> Αυτό είναι ένα παράδειγμα.  
> auto einai ena paradeigma.  
> ‘This is an example.’

### 引用

文内引用以括号形式出现，如 (Gusfield, 1997)；若作者名已在句中出现：Gusfield (1997)。年份歧义时在小写字母区分。两位作者写全两名 (Aho and Ullman, 1972)；三位及以上用第一作者加 “et al.” (Chandra et al., 1981)。多条引用合并为一组括号 (Gusfield, 1997; Aho and Ullman, 1972)。

勿将完整引用作为句子成分。勿写

> (Gusfield, 1997) showed that ...  
> In (Gusfield, 1997), ...''

应写

> Gusfield (1997) showed that ...  
> In Gusfield (1997), ...

投稿应准确引用先前与相关工作，包括代码与数据。若先前工作发表于多个场合，应引用经同行评审的存档版本。若存在多个版本，应引用作者实际使用的版本。

### 致谢

致谢紧挨参考文献之前。致谢节不编号。审稿版不得包含本节。

### 参考文献

在无编号章节标题 **References** 下集中列出全部参考文献。References 置于任何附录之前。按第一作者姓氏字母序排列，而非按文中出现顺序。

尽量提供完整、格式一致的引用，例如 [Computational Linguistics 期刊格式](http://cljournal.org/style_guide_refs.html) 或 [APA 出版手册](https://apastyle.apa.org/products/publication-manual-7th-edition) 第七版。作者写全名，勿仅写首字母。勿依赖自动引文索引提供准确条目。

作为推动 ACL 材料在学界外被更广泛引用的一项工作，ACL 已注册为 CrossRef 成员，可为学术材料注册 DOI（数字对象标识符）。

在可能的情况下，所有引用须含被引文献的 DOI；其次可链接至 ACL Anthology 页面。多数材料可在当前 [ACL Anthology](https://aclweb.org/anthology/) 中找到对应记录。

期刊论文示例：

> Rie Kubota Ando and Tong Zhang. 2005. [A framework for learning predictive structures from multiple tasks and unlabeled data](https://www.jmlr.org/papers/v6/ando05a.html). *Journal of Machine Learning Research*, 6:1817–1853.

非 ACL 会议论文示例（含 DOI）：

> Galen Andrew and Jianfeng Gao. 2007. [Scalable training of L1-regularized log-linear models](https://doi.org/10.1145/1273496.1273501). In *Proceedings of the 24th International Conference on Machine Learning*, pages 33–40.

ACL Anthology 论文示例（含 DOI）：

> James Goodman, Andreas Vlachos, and Jason Naradowsky. 2016. [Noise reduction and targeted exploration in imitation learning for Abstract Meaning Representation parsing](http://dx.doi.org/10.18653/v1/P16-1001). In *Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 1–45711, Berlin, Germany. Association for Computational Linguistics.

ACL Anthology 论文示例（无 DOI）：

> Benjamin Börschinger and Mark Johnson. 2011. [A particle filter algorithm for Bayesian word segmentation](https://www.aclweb.org/anthology/U11-1004/). In *Proceedings of the Australasian Language Technology Association Workshop 2011*, pages 10–44718, Canberra, Australia.

arXiv 论文示例：

> Mohammad Sadegh Rasooli and Joel R. Tetreault. 2015. [Yara parser: A fast and accurate dependency parser](http://arxiv.org/abs/1503.06733). *Computing Research Repository*, arXiv:1503.06733. Version 2.

## 附录

附录为可读材料，含对理解正文非关键的引理、公式、证明与表格等。按字母顺序编号并给出信息性标题，例如：

> Appendix A. Title of Appendix

附录位于参考文献之后。

附录审稿版须遵守与正文相同的匿名规则。

## 补充材料

投稿可包含论文中描述但不可直接阅读的补充材料。随附软件与/或数据应含许可证及适当的研究审查说明。补充材料可记录预处理决策、模型参数及复现实验所需的其他细节。看似微小的预处理有时对性能影响巨大，故须精确记录以刻画最先进方法。

尽管如此，补充材料应起**补充**而非**核心**作用。**滥用补充材料的投稿可能不经审稿即被拒。** 补充材料可含放不进正文的证明或推导细节、特征或模板列表、系统样例输入输出、伪代码或源代码及数据等。（源代码与数据应单独上传，而非并入正文 PDF。）

正文不得依赖补充材料：正文可引用补充材料，审稿人可获取，但不会被要求评审补充材料。

补充材料审稿版须遵守与正文相同的匿名规则。

## 致谢贡献者

本文改编自早期 ACL 与 NAACL 论文集说明，包括
ACL 2020（Steven Bethard、Ryan Cotterell、Rui Yan）、
ACL 2019（Douwe Kiela、Ivan Vulić）、
NAACL 2019（Stephanie Lukin、Alla Roskovskaya）、
ACL 2018（Shay Cohen、Kevin Gimpel、Wei Lu）、
NAACL 2018（Margaret Mitchell、Stephanie Lukin）、
(NA)ACL 2017/2018 BibTeX 建议（Jason Eisner）、
ACL 2017（Dan Gildea、Min-Yen Kan）、
NAACL 2017（Margaret Mitchell）、
ACL 2012（Maggie Li、Michael White）、
ACL 2010（Jing-Shin Chang、Philipp Koehn）、
ACL 2008（Johanna D. Moore、Simone Teufel、James Allan、Sadaoki Furui）、
ACL 2005（Hwee Tou Ng、Kemal Oflazer）、
ACL 2002（Eugene Charniak、Dekang Lin），
以及更早由 John Chen、Henry S. Thompson、Donald Walker 等人撰写的 ACL/EACL 格式说明。
部分内容取自 *International Joint Conference on Artificial Intelligence* 与 *Conference on Computer Vision and Pattern Recognition* 的排版说明。
