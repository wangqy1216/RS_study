## RS15 Thinking
**1. CTR数据中的类别数据处理，编码方式有哪些，区别是什么**

答：（1）编码方式：Label Encoder和One-hot Encoder。

（2）区别： 1）Label Encoder是将类别数据用数值编号来表示；One-Hot编码，又称为一位有效编码，是采用N位状态寄存器来对类别数据的N个状态进行编码，每个状态都由他独立的寄存器位，并且在任意时候只有一位有效。2）LabelEncoder编码占用内存小；One-Hot编码将离散特征的取值扩展到了欧式空间，且到原点是等距的，因此可以避免让非偏序关系的类别数据取值具有偏序性，不过当类别种类特别多时，可能会使得数据非常稀疏。

**2. 对于时间类型数据，处理方法有哪些**

答：（1）持续时间统计：如统计页面浏览时长；（2）间隔时间统计：如上次购买/点击离现在的时长；（3）时间特征拆解：年、月、日、时、分、秒、星期几、哪个季节、哪个周、一天哪个时间段等；（4）时间特征判断：是否闰年、是否年初、是否年尾、是否周末、是否节假日；（5）时间聚合：如按月统计某一特征均值。

**3.  你是如何理解CTR预估中的特征组合的，请举例说明**

答：特征对于CTR预估至关重要，除了原始特征，进行特征的组合生成新的特征能够挖掘到一些新的信息，从而提升预测效果。如性别和年龄特征的组合可以形成新的用户特征。

**4.  DCN和xDeepFM都可以进行自动特征组合，有何区别**

答：DCN在进行自动特征组合时是基于元素级别进行交叉，即为bit-wise；而XDeepFM在进行自动特征组合时是基于向量级别进行交叉，即为vector-wise，相比DCN,不会破坏特征向量原本的物理含义。同时，DCN仅在输出层输出全部结果，而xDeepFM则在每一层都会输出中间结果。

**5.  今天讲解的特征组合只是特征工程中的一部分，你理解的特征工程都包括哪些，不防做个思维导图**

答：详见特征工程.png