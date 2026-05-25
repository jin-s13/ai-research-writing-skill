# 引言版本 4：应用开篇并暴露挑战

`版本 4：若任务已熟悉，可直接介绍应用，并在开篇通过前人方法暴露目标技术挑战。`

专家要点（忠实译述）：

1. 若开篇段落已点明要解决的问题，往往更好。
2. 但此风格需合适条件，较不常见。
3. 通常仍需若干段前人工作，目标挑战才会清晰。

```latex
% Introduce Application
%% Example 1: Reconstructing 3D scenes from multi-view images is a cornerstone of many applications such as augmented reality, robotics, and autonomous driving.
%% Example 2: Instance segmentation is the cornerstone of many computer vision tasks, such as video analysis, autonomous driving, and robotic grasping, which require both accuracy and efficiency.

% Use previous methods to expose the target technical challenge
%% Example 1: Given input images, traditional methods [43, 44, 59] generally estimate the depth map for each image based on the multi-view stereo (MVS) algorithms and then fuse estimated depth maps into 3D models. Although these methods achieve successful reconstruction in most cases, they have difficulty in handling low-textured regions, e.g., floors and walls of indoor scenes, due to the unreliable stereo matching in these regions.
%% Example 2: Most of the state-of-the-art instance segmentation methods [18, 27, 5, 19] perform pixel-wise segmentation within a bounding box given by an object detector [36], which may be sensitive to the inaccurate bounding box. Moreover, representing an object shape as dense binary pixels generally results in costly post-processing.
```
