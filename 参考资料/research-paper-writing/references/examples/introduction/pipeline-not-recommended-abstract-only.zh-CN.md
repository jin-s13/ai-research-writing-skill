# 不推荐：Introduction 中仅写抽象方法描述

`不推荐：若方法较简单，不要在 Introduction 中回避具体方法细节、只讨论抽象洞见来显得新颖。`

专家要点（忠实译述）：

1. 此写作模板的技巧在于如何让简单 pipeline 听起来新颖。
2. 注意：这不是让洞见显得新颖，而是让 pipeline 步骤显得新颖。
3. 多数情况下不推荐。
4. 更好目标是在 Introduction 中清楚解释核心贡献如何实现。

```latex
% To tackle this problem, we propose a novel 3D GAN training method to generate photo-realistic images irrespective of the viewing angle.

% Introduce key idea
% Our key idea is as follows. To ease the challenging problem of learning photorealistic and multi-view consistent image synthesis, we cast the problem into two subproblems, each of which can be solved more easily.

% Explain why the key idea works, but without concretely discussing the full pipeline (or only discuss abstract benefit)
%% Example: Specifically, we formulate the problem as a combination of two simple discrimination problems, one of which learns to discriminate whether a synthesized image looks real or not, and the other learns to discriminate whether a synthesized image agrees with the camera pose. Unlike the formulations of the previous methods, which try to learn the real image distribution for each pose, or to learn pose estimation, our subproblems are much easier as each of them is analogous to a basic binary classification problem.

% Introduce pipeline modules with new terms but without clearly explaining the full pipeline (or skip concrete pipeline details)
%% Example: Based on this key idea, we propose a dual-branched discriminator, which has two branches for learning photorealism and pose consistency, respectively. As these branches are supervised explicitly for their respective purposes, high-quality images with pose consistency can be produced at each viewing angle, and consequently, the generator creates high-quality images and shapes. (This paragraph does not clearly explain how the pipeline works.)

% Introduce another contribution
%% Example: In addition, we propose a pose-matching loss to give supervision to the discriminator for the pose consistency, by considering a positive pose (i.e., rendering pose or ground truth pose) and a negative pose (i.e., irrelevant pose) for a given image. (This paragraph does not clearly explain how the pipeline works.)

% Explain expected benefit over prior methods
%% Example: For example, the frontal viewpoint is one of the irrelevant poses for a side-view image. As reported in the experiments, this loss helps improve image and shape quality. This can be interpreted as a simplification of a classification problem from a large number of classes into binary, which is composed of positive and negative pairs.
```
