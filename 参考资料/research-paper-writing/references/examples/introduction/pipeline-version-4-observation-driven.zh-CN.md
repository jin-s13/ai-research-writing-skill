# Pipeline 版本 4（观察驱动贡献）

`版本 4：贡献来自一项重要观察。先介绍关键创新，再以直观观察作动机，然后写方法细节与益处。`

```latex
% In this paper, we propose a learning-based snake algorithm, named deep snake, for real-time instance segmentation.

% Our innovation is introducing the circular convolution for efficient feature learning on a contour, as illustrated in Figure 1.

% We observe that the contour is a cycle graph that consists of a sequence of vertices connected in a closed cycle. Since every vertex has the same degree equal to two, we can apply the standard 1D convolution on the vertex features.

% Considering that the contour is periodic, deep snake introduces the circular convolution, which indicates that an aperiodic function (1D kernel) is convolved in the standard way with a periodic function (features defined on the contour).

% The kernel of circular convolution encodes not only the feature of each vertex but also the relationship among neighboring vertices. In contrast, the generic GCN performs pooling to aggregate information from neighboring vertices. The kernel function in our circular convolution amounts to a learnable aggregation function, which is more expressive and results in better performance than using a generic GCN, as demonstrated by our experimental results in Section 5.2.
```
