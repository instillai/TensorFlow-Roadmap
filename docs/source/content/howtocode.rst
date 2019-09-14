============================
Programming with TensorFlow
============================

.. * `Title`_: some text
.. .. _Title: link

The references here, deal with the details of programming and writing TensorFlow code.

-------------------------------
Reading data and input pipeline
-------------------------------

The first part is always how to prepare data and how to provide the pipeline to feed it to TensorFlow.
Usually providing the input pipeline can be complicated, even more than the structure design!

~~~~~~~~~~~~~~~~~
Written resources
~~~~~~~~~~~~~~~~~

* `Dataset API for TensorFlow Input Pipelines`_: A TensorFlow official documentation on *Using the Dataset API for TensorFlow Input Pipelines*
* `TesnowFlow input pipeline`_: Input pipeline provided by Stanford.
* `TensorFlow input pipeline example`_: A working example.
* `TensorFlow Data Input`_: TensorFlow Data Input: Placeholders, Protobufs & Queues
* `Reading data`_: The official documentation by the TensorFLow on how to read data
* `basics of reading a CSV file`_: A tutorial on reading a CSV file
* `Custom Data Readers`_: Official documentation on this how to define a reader.

.. _Dataset API for TensorFlow Input Pipelines: https://github.com/tensorflow/tensorflow/tree/v1.2.0-rc1/tensorflow/contrib/data
.. _TesnowFlow input pipeline: http://web.stanford.edu/class/cs20si/lectures/slides_09.pdf
.. _TensorFlow input pipeline example: http://ischlag.github.io/2016/06/19/tensorflow-input-pipeline-example/
.. _TensorFlow Data Input: https://indico.io/blog/tensorflow-data-inputs-part1-placeholders-protobufs-queues/
.. _Reading data: https://www.tensorflow.org/programmers_guide/reading_data
.. _basics of reading a CSV file: http://learningtensorflow.com/ReadingFilesBasic/
.. _Custom Data Readers: https://www.tensorflow.org/extend/new_data_formats

~~~~~~~~~~~~~~~~
Visual resources
~~~~~~~~~~~~~~~~

* `Tensorflow tutorial on TFRecords`_: A tutorial on how to transform data into TFRecords

.. _Tensorflow tutorial on TFRecords: https://www.youtube.com/watch?v=F503abjanHA

----------
Variables
----------

Variables are supposed to hold the parameters and supersede by new values as the parameters are updated.
Variables must be clearly set and initialized.

~~~~~~~~~~~~~~~~~
Written Resources
~~~~~~~~~~~~~~~~~

^^^^^^^^^^^^^^^^^^^^^^^^
Creation, Initialization
^^^^^^^^^^^^^^^^^^^^^^^^

* `Variables Creation and Initialization`_: An official documentation on setting up variables
* `Introduction to TensorFlow Variables - Creation and Initialization`_: This tutorial deals with defining and initializing TensorFlow variables
* `Variables`_: An introduction to variables

.. _Variables Creation and Initialization: https://www.tensorflow.org/programmers_guide/variables
.. _Introduction to TensorFlow Variables - Creation and Initialization: http://machinelearninguru.com/deep_learning/tensorflow/basics/variables/variables.html
.. _Variables: http://learningtensorflow.com/lesson2/

^^^^^^^^^^^^^^^^^^^^^
Saving and restoring
^^^^^^^^^^^^^^^^^^^^^

* `Saving and Loading Variables`_: The official documentation on saving and restoring variables
* `save and restore Tensorflow models`_: A quick tutorial to save and restore Tensorflow models

.. _Saving and Loading Variables: https://www.tensorflow.org/programmers_guide/variables
.. _save and restore Tensorflow models: http://cv-tricks.com/tensorflow-tutorial/save-restore-tensorflow-models-quick-complete-tutorial/

^^^^^^^^^^^^^^^^^
Sharing Variables
^^^^^^^^^^^^^^^^^

* `Sharing Variables`_: The official documentation on how to share variables

.. _Sharing Variables: https://www.tensorflow.org/programmers_guide/variable_scope

~~~~~~~~~~~~~~~~~
Visual Resources
~~~~~~~~~~~~~~~~~

* `Deep Learning with Tensorflow - Tensors and Variables`_: A Tensorflow tutorial for introducing Tensors, Variables and Placeholders
* `Tensorflow Variables`_: A quick introduction to TensorFlow variables
* `Save and Restore in TensorFlow`_: TensorFlow Tutorial on Save and Restore variables

.. _Deep Learning with Tensorflow - Tensors and Variables: https://www.youtube.com/watch?v=zgV-WzLyrYE
.. _Tensorflow Variables: https://www.youtube.com/watch?v=UYyqNH3r4lk
.. _Save and Restore in TensorFlow: https://www.tensorflow.org/programmers_guide/variable_scope

--------------------
TensorFlow Utilities
--------------------

Different utilities empower TensorFlow for faster computation in a more monitored manner.

~~~~~~~~~~~~~~~~~
Written Resources
~~~~~~~~~~~~~~~~~

^^^^^^^^^^
Supervisor
^^^^^^^^^^

* `Supervisor - Training Helper for Days-Long Trainings`_: The official documentation for TensorFLow Supervisor.
* `Using TensorFlow Supervisor with TensorBoard summary groups`_: Using both TensorBoard and the Supervisor for profit
* `Tensorflow example`_: A TensorFlow example using Supervisor.


.. _Supervisor - Training Helper for Days-Long Trainings: https://www.tensorflow.org/programmers_guide/supervisor
.. _Using TensorFlow Supervisor with TensorBoard summary groups: https://dev.widemeadows.de/2017/01/21/using-tensorflows-supervisor-with-tensorboard-summary-groups/
.. _Tensorflow example: http://codata.colorado.edu/notebooks/tutorials/tensorflow_example_davis_yoshida/

^^^^^^^^^^^^^^^^^^^
TensorFlow Debugger
^^^^^^^^^^^^^^^^^^^

* `TensorFlow Debugger (tfdbg) Command-Line-Interface Tutorial`_: Official documentation for using debugger for MNIST
* `How to Use TensorFlow Debugger with tf.contrib.learn`_: A more high-level method to use the debugger.
* `Debugging TensorFlow Codes`_: A Practical Guide for Debugging TensorFlow Codes
* `Debug TensorFlow Models with tfdbg`_:  A tutorial by Google Developers Blog


.. _TensorFlow Debugger (tfdbg) Command-Line-Interface Tutorial: https://www.tensorflow.org/programmers_guide/debugger
.. _How to Use TensorFlow Debugger with tf.contrib.learn: https://www.tensorflow.org/programmers_guide/tfdbg-tflearn
.. _Debugging TensorFlow Codes: https://github.com/wookayin/tensorflow-talk-debugging
.. _Debug TensorFlow Models with tfdbg: https://developers.googleblog.com/2017/02/debug-tensorflow-models-with-tfdbg.html

^^^^^^^^^^
MetaGraphs
^^^^^^^^^^

* `Exporting and Importing a MetaGraph`_: Official TensorFlow documentation
* `Model checkpointing using meta-graphs in TensorFlow`_: A working example

.. _Exporting and Importing a MetaGraph: https://www.tensorflow.org/programmers_guide/meta_graph
.. _Model checkpointing using meta-graphs in TensorFlow: http://www.seaandsailor.com/tensorflow-checkpointing.html

^^^^^^^^^^^
Tensorboard
^^^^^^^^^^^

* `TensorBoard - Visualizing Learning`_: Official documentation by TensorFlow.
* `TensorFlow Ops`_: Provided by Stanford
* `Visualisation with TensorBoard`_: A tutorial on how to create and visualize a graph using TensorBoard
* `Tensorboard`_: A brief tutorial on Tensorboard

.. _TensorBoard - Visualizing Learning: https://www.tensorflow.org/get_started/summaries_and_tensorboard
.. _TensorFlow Ops: http://web.stanford.edu/class/cs20si/lectures/notes_02.pdf
.. _Visualisation with TensorBoard: http://learningtensorflow.com/Visualisation/
.. _Tensorboard: http://edwardlib.org/tutorials/tensorboard

~~~~~~~~~~~~~~~~~
Visual Resources
~~~~~~~~~~~~~~~~~

* `Hands-on TensorBoard (TensorFlow Dev Summit 2017)`_: An introduction to the amazing things you can do with TensorBoard
* `Tensorboard Explained in 5 Min`_: Providing the code for a simple handwritten character classifier in Python and visualizing it in Tensorboard
* `How to Use Tensorboard`_: Going through a bunch of different features in Tensorboard


.. _Hands-on TensorBoard (TensorFlow Dev Summit 2017): https://www.youtube.com/watch?v=eBbEDRsCmv4
.. _Tensorboard Explained in 5 Min: https://www.youtube.com/watch?v=3bownM3L5zM
.. _How to Use Tensorboard: https://www.youtube.com/watch?v=fBVEXKp4DIc
