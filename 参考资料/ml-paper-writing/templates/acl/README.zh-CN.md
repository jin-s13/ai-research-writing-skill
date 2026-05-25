# *ACL 论文样式

本目录包含最新版 *ACL 会议 LaTeX 模板。

## 作者须知

向 *ACL 会议投稿的论文必须使用官方 ACL 样式模板。

LaTeX 样式文件可通过以下方式获取：

- [Overleaf 模板](https://www.overleaf.com/latex/templates/association-for-computational-linguistics-acl-conference/jvxskxpnznfj)
- 本仓库
- [.zip 压缩包](https://github.com/acl-org/acl-style-files/archive/refs/heads/master.zip)

示例请参见 [`acl_latex.tex`](https://github.com/acl-org/acl-style-files/blob/master/acl_latex.tex)。

请遵循适用于 *ACL 各会议的通用排版指南：

- [论文排版指南](https://acl-org.github.io/ACLPUB/formatting.html)

作者不得修改这些样式文件，也不得使用为其他会议设计的模板。

## 出版主席须知

若需为会议定制样式文件，请 fork 本仓库并进行必要修改。至少应更新会议名称并重命名相关文件。

若对模板做了应传播至后续会议的改进，请提交 pull request。提前致谢！

在旧版模板中，作者需填写 START 投稿 ID，以便在匿名版每页页眉加盖该编号。现已不再需要：START 系统可自动完成加盖。目前程序主席可向 support@softconf.com 发邮件申请启用该功能。

## 修改样式文件的流程

- 在 GitHub 上合并 pull request，或推送到 GitHub
- 从 GitHub 将更新 pull 到本地仓库
- 再将本地仓库推送到 Overleaf 项目
    - Overleaf 项目：https://www.overleaf.com/project/5f64f1fb97c4c50001b60549
    - Overleaf git 地址：https://git.overleaf.com/5f64f1fb97c4c50001b60549
- 在 Overleaf 中点击 “Submit”，再点击 “Submit as Template”，以便请 Overleaf 根据该项目更新公开模板
