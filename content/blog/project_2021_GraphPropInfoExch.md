title:      						Graph Property Driven Information Exchange in Distributed Networks
id:                 				project_0100
date:       						2021/06/22 20:00
category:		    				Project
categories:		    				Project
tags:       						Distributed Networks, Graph Theory, Graph Properties, Decentralization, Protocol, Math, CS, Mathematical Computer Science, Project
author:     						Carolin Zöbelein
slug_dir:           				Projects
slug_subdir:        				2021
slug:       						Graph-Property-Driven-Information-Exchange-in-Distributed-Networks
index_title:						Graph Property Driven Information Exchange in Distributed Networks
index_image:        				/images/Project.jpg
sum_image:							/images/Project.jpg
kind:               				Project
project_period:     				Since 2021/03/01
project_members:    				Carolin Zöbelein
keywords:           				distributed networks, graph theory, graph properties, decentralization, protocol, math, cs, mathematical computer science




Graph property driven information exchange is a new mathematical concept for describing data flow in distributed networks. It bases on five fundamentals.


> Fundamental 1 (Universality $\mathbf{F_{uni}}$). *All characteristics of a network participant are describable by the same mathematical structure (everything is considered to be an 'object').*

> Fundamental 2 (Duality $\mathbf{F_{dua}}$). *Network topologies and characteristics of network participants are mathematical describable by the same mathematical object structure.*

> Fundamental 3 (Vicariousness $\mathbf{F_{vic}}$). *Data information exchange doesn't happen directly. It happens indirectly by property or property information exchange.*

> Fundamental 4 (Property Driven $\mathbf{F_{prd}}$). *Protocol states are (equilibrium) states of graph properties. Properties are the driving force of each network protocol living on a distributed network which is based on the fundamentals 1, 2 and 3.*

> Fundamental 5 (Physical Realness $\mathbf{F_{phr}}$). *Property driven disributed networks can be represented by physical structures initiated by fundamental 4.*



This fundamentals are derived by already existing models (see also the following section 'Background'), and finally connected by an enhancement of graph theory which we introduce by our work.



<h3>Background</h3>

We give a recap of three existing, math orientated, models for description and analysis of distributed networks.

<h5><i>Graph Models</i></h5>
The most known model for describing distributed networks is given by graph theory. Let $G = \left(V, E\right)$ be a *graph* with a finite set of *vertices* $v_{i} \in V$ and *edges* $e_{k} = \left(v_{i}, v_{j}\right) \in E$ with $E := V \times V$. We identify vertices, also called nodes, with participants (clients and servers) of the network and edges with communication channels between them, which forms the individual topology of the system. Given such a basic graph description, we can enhance it by several properties observed in context of distributed networks [1].

Assume each participant of the network run its communication over several open *ports*, then we can define a *port-numbered network* by a triple $N = \left(V, P, p\right)$, with $V$ be the set of vertices, $P$ be the set of ports, and $p : P \rightarrow P$ be a function that gives us the connections between ports, so that each port is given by a pair $\left(v_{i},q_{i}\right)$, where $v_{i} \in V$ and $q_{i} \in \{1, 2, \dots \}$. We call this a *port-numbering model (PN model)* [1]. Furthermore, if we assign *unique identifiers* for a port-numbered network by an injection $id : V \rightarrow \{1, 2, \dots, |V|^{c} \}$, for a fix constant $c > 1$, so that each vertex $v_{i} \in V$ is labeled with an unique integer, with labels which are assumed to be relatively small, we call this a *network with unique identifiers (LOCAL model)* [1]. Finally, we assume a *bandwidth restriction* in each communication round, over each edge, so that we are only able to send $\mathcal{O}\left(\log\left(|V|\right)\right)$-bit messages $\mathrm{Msg}_{A}$ encoded as natural numbers $\mathbb{N}$ on a distributed algorithm $A$. We call this a *bandwidth restriction model (CONGEST model)* [1].


<h5><i>Combinatorial Topology</i></h5>

In the 1990s *combinatorial topology*, an *extending graph theory to higher dimensional objects*, was shown to provide a framework for a large variety of distributed computing models [2] [3]. It represents all possible executions of a distributed algorithm as well as the relations between them, as a single mathematical object, whose properties reflect the solvability of a problem and primary used to study failure-tolerant networks in the context of shared memory and message passing systems.


<center>
    ![Combinatorial Topology Example](/images/projects/combinatoricaltopology.png)
</center>

<center>
    <b style="font-size: 0.85em;">Figure 1: Example for a combinatorical topology model. Impact of the information-flow graph on the protocol complex for a binary consensus with three processes. Labels give the input and output values, in the input and output complexes respectively, or views in protocol complexes [3].</b>
</center>


In this concept, all possible input (output) configurations are modelled as a single object called *input (output) complex* (see figure 1 first respectively fourth graph), specifying a task as a relation between the input and output complexes. Computation results in a *topological deformation* that modifies this complexes into another complex, called *protocol complex* (see figure 1 second respectively third graph). A task is solvable in a computational model if and only if there exists a simplicial map, called *decision map*, given by the protocol complex to the output complex. For every input configuration, the execution of an algorithm leads to one or many system configurations, which equals a subcomplex of the protocol complex, and the decision map, maps every of this configurations of the subcomplex into a, legal for the given input, configuration of the output complex. The understanding of distributed algorithms lies in the understanding of topological deformations and decision maps [3].



<h5><i>Algebraic Structures</i></h5>

Apart from graph theory also other models for distributed networks have been considered [4] like an alternative characterisation of object-based distributed systems in terms of algebraic structures [5]. Here, *objects* represent an abstraction for distinct types of entities, such as humans, intelligent agents, accounts, software components or processing units. By the usage of a *temporal logic language*, they specify *local object behaviours* by *local constraints*, which restrict the set of life cycles admissible for each object. During in other models participants interact by asynchronous messages communications (receiving, manipulation, sending), here, objects comply with *synchronous*, *event based interaction* [5].

The algebra is given by some basic definitions, like for time which is considered by *time frames*, a ($n$ algebraic) structure $\langle\langle T, \leq \rangle,L\rangle$ (reflexiv, anti-symmetric and transitive), where $L$ is a set of *linear time flows* (linear, injective, surjective, monotone), for *object structures*, a $5$-tuple $\langle \mathcal{T}, \mathcal{V}, \mathcal{L}, B, P \rangle$ in terms of the disjoint non-empty sets $\mathbf{T}$ (time domain), $\mathbf{Ev}$ (event domain) and $\mathbf{Loc}$ (location domain), with $\mathcal{T}$ be a time frame, $\mathcal{V}$ be an *event structure* in terms of event domain $\mathbf{Ev}$, $\mathcal{L}$ be a *location structure* in terms of location domain $\mathbf{Loc}$, $B : \mathbf{Ev} \rightarrow \mathcal{P}\left(\mathcal{I}_{+}\left(\mathrm{cod} \ L\right)\right)$ be a *behaviour* and $P : \mathbf{Loc} \rightarrow \mathcal{P}\left(\mathcal{I}_{+}\left(\mathrm{cod} \ L\right)\right)$ be a *placement* ($\mathcal{P}\left(X\right)$ be the set of all subsets of $X$, $\mathcal{I}\left(X\right)$ be the of all open intervals in terms of $X$). Finally, a *distributed system model* is given by a $4$-tuple $\langle \mathcal{O}, E, I, C \rangle$, with $\mathcal{O}$ be an *object universe*, a countable set of object structures, $E : \mathcal{O} \rightarrow \mathbf{Bool}$ be an *environment* identification function, $I : \mathcal{O} \rightarrow \mathbf{Bool}$ be an *internal object* identification function, and $C : \mathcal{O} \rightarrow \mathcal{O}$ be a partial map which induces a family of *time correlation functions* [5].


<h3>References</h3>

[1] Juho Hirvonen and Jukka Suomela. 2020. Distributed Algorithms 2020. Aalto University, Finland. <a href="https://jukkasuomela.fi/da2020/" title="External: Distributed Algorithms" target="_blank">https://jukkasuomela.fi/da2020/</a>, <a href="https://jukkasuomela.fi/da2020/da2020.pdf" title="External: Distributed Algorithms - .pdf" target="_blank">https://jukkasuomela.fi/da2020/da2020.pdf</a>.

[2] Maurice Herlihy, Dmitry Kozlov, and Sergio Rajsbaum. 2013. Distributed computing through combinatorial topology. Newnes.

[3] Armando Castañeda, Pierre Fraigniaud, Ami Paz, Sergio Rajsbaum, Matthieu Roy, and Corentin Travers. 2021. A topological perspective on distributed network algorithms. Theoretical Computer Science 849 (2021), 121–137.

[4] Leslie Lamport and Nancy Lynch. 1990. Distributed computing: Models and methods. In Formal models and semantics. Elsevier, 1157–1199.

[5] Carlos Henrique C Duarte. 2011. Mathematical models of object-based distributed systems. In Formal Modeling: Actors, Open Systems, Biological Systems. Springer, 57–73.


