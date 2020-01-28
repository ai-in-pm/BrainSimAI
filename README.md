# BrainSimII
Neural Simulator for AGI research and development

I appreciate your interest in this product and hope your experience will be positive.

Brain Simulator II is an open-source, free package which simulates an array of simple "neurons" coupled with "modules" which allow any group of neurons to be backed by code.

Strategy:
Brain Simulator II is an experimental platform. The point is to be able to try out different AGI algorithms and architectures with a minimum of effort to see what works well and what doesn't. It's not intended to be an application or development toolkit. There may never be a stable release, there may never be fully-debugged code...so patience and a degree of expertise are required.
Development is incremental. Write a single bit of functionality, try it out, see if it makes the system better. While there is no grand plan, there is an overall strategy of a set of modules which may result in an AGI system. Accordinly, the modular system can continue to work even if other developers includ modules which aren't functional yet. In fact, the project includes several modules which are not currently useful but which may prove useful in the future.

Neurons and Synapses:
Neurons are tiny blocks of code interconnected by synapses. A synapse is owned by a neuron and connects to a target neuron with a weight. A neuron has a single function...it can fire. When it fires, it sends a single-value signal to every neuron in its list of synapse targets...and the message is the weight of the synapse. There are several neuron models.

Modules:
A module is a rectangular array of neurons which is contolled by code. While the neurons are still functional, the code can easily perform calculations which would be tedious in the basic neuron models.
