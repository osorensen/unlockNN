.. currentmodule:: unlocknn.model

Probabilistic models
====================

UnlockNN includes an extensible interface for adding uncertainty quantification
to any trained keras model using a
`variational Gaussian process <https://www.tensorflow.org/probability/api_docs/python/tfp/distributions/VariationalGaussianProcess>`_
(VGP). A VGP is a modification of a `Gaussian process <https://distill.pub/2019/visual-exploration-gaussian-processes>`_
that vastly improves model scalability; instead of using the entire training dataset
as index points, a VGP uses variational inference to compute a smaller set of *inducing* index
points that lead to a good approximation of the "full" Gaussian process.

By supplanting the last layer(s) of a keras model with a VGP, the model's
predictions become Gaussian distributions, rather than tensors. The mean of
this distribution is the *de facto* "prediction" and the standard
deviation indicates uncertainty. For example, two standard deviations
gives the 95% confidence interval.

.. important::
    The caveat of using a VGP is that the probabilistic model must undergo
    further training to determine the inducing index point
    locations and the kernel parameters, which can be expensive!

The module also contains a specific implementation for use with
`MEGNet <https://github.com/materialsvirtuallab/megnet>`_, a highly performant
graph neural network model for materials property prediction, with the
:class:`MEGNetProbModel`.

The ProbNN API
^^^^^^^^^^^^^^

To add uncertainty quantification to an arbitrary Keras model,
you should create a class that inherits from :class:`ProbNN`
and implements :meth:`ProbNN.train`, as well as appending
any variables that are necessary for reloading the model
to :attr:`ProbNN.CONFIG_VARS`.

.. autoclass:: ProbNN
    :members:

MEGNet probabilistic model
--------------------------

Use :class:`MEGNetProbModel` to add uncertainty quantification
to a :class:`MEGNetModel`:

.. autoclass:: MEGNetProbModel
    :members: train, predict, evaluate, save, load, set_frozen, nn_frozen, norm_frozen, vgp_frozen
