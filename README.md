_*MultiVeStA*_ is an efficient statistical analysis tool which can be easily integrated with existing discrete event simulators, enriching them with distributed Statistical Analysis and Statistical Model Checking capabilities.

The tool is maintained and developed by Stefano Sebastio and [Andrea Vandin](http://www.ecs.soton.ac.uk/people/av1v13). The tool comes as an extension of the existing VeStA and PVeStA tools, developed at the Department of Computer Science at the University of Illinois at Urbana-Champaign.

The currently supported discrete event simulators are (in alphabetic order):
   * [Alchemist](http://apice.unibo.it/xwiki/bin/view/Alchemist/): _a simulator targeting chemical-oriented computational systems_
   * [ARGoS](http://iridia.ulb.ac.be/argos/): _a multi-robot, multi-engine simulator for heterogeneous Swarm robotics_ 
   * [Bio-PEPA](http://www.biopepa.org/ Bio-PEPA): _a language for the modelling and the analysis of biochemical networks_
   * [DEUS](http://code.google.com/p/deus/ DEUS): _a general-purpose, open-source, simulator for the analysis of large scale systems_
   * [QFLan](https://code.google.com/p/multivesta/wiki/QFLan): _a probabilistic feature-oriented language with quantitative constraints for product families_
   * [MISSCEL](http://sysma.lab.imtlucca.it/misscel/): _an interpreter and simulator for the Service Component Ensemble Language_
   * Any python simulator, resorting to [Py4J](http://py4j.sourceforge.net/)
   * [Probabilistic Maude](http://www.sciencedirect.com/science/article/pii/S1571066106002672): _an engine to execute probabilistic rewrite theories_
   * A built in DTMC and CTMC engine




   * _other simulators coming soon_
   * _*...and yours with just few lines of code*_ (just [contact us!](mailto:a.vandin@soton.ac.uk;stefano.sebastio@imtlucca.it)).


Download [MultiVeStA](https://docs.google.com/file/d/0B1wH4SBkfGwYUklocFMtSWlIMkU/edit?usp=sharing), and check the [http://code.google.com/p/multivesta/w/list Wiki page] of this site for guidelines on using it (or just [contact us!](mailto:andrea.vandin@imtlucca.it;stefano.sebastio@imtlucca.it)).

== Papers ==
   * [MultiVeStA: Statistical Model Checking for Discrete Event Simulators](http://dl.acm.org/citation.cfm?id=2631884) (*please cite this work*) in the proceedings of _VALUETOOLS'13_ ([extended version](http://eprints.imtlucca.it/1798/))
   * [Statistical Analysis of Probabilistic Models of Software Product Lines with Quantitative Constraints](https://www.dropbox.com/s/qty17idt76lbaie/SPLC15.pdf?dl=0) in the proceedings of _  SPLC'15 _
   * [Quantitative Analysis of Probabilistic Models of Software Product Lines with Statistical Model Checking](http://arxiv.org/ct?url=http%3A%2F%2Fdx.doi.org%2F10%252E4204%2FEPTCS%252E182%252E5&v=3359e1fe) in the proceedings of _  FMSPLE'15 _
   * [An Analysis Pathway for the Quantitative Evaluation of Public Transport Systems](http://link.springer.com/chapter/10.1007%2F978-3-319-10181-1_5)  in the proceedings of _  IFM'14 _
   * [Distributed statistical analysis of complex systems modeled through a chemical metaphor](http://eprints.imtlucca.it/1697/)  in the proceedings of _  HPCS'14 _
   * [Reasoning (on) Service Component Ensembles in Rewriting Logic](http://link.springer.com/chapter/10.1007%2F978-3-642-54624-2_10) in the proceedings of _  SAS'14 _
   * [A Computational Field Framework for Collaborative Task Execution in Volunteer Clouds](http://dx.doi.org/10.1145/2593929.2593943) in the proceedings of _ SEAMS'14 _
   * [Reputation-based Cooperation in the Clouds](http://dx.doi.org/10.1007/978-3-662-43813-8_15) in the proceedings of _ IFIPTM'14 _


   

== Other Related Papers ==   
   * [VESTA: A Statistical Model-checker and Analyzer for Probabilistic Systems](http://www.computer.org/csdl/proceedings/qest/2005/2427/00/24270251-abs.html)
   * [PVeStA: A Parallel Statistical Model Checking and Quantitative Analysis Tool](http://link.springer.com/chapter/10.1007%2F978-3-642-22944-2_28)
   * [PMaude: Rewrite-based Specification Language for Probabilistic Object Systems](http://www.sciencedirect.com/science/article/pii/S1571066106002672)


== Acknowledgments ==
Our work is developed within and supported by the European projects [QUANTICOL](http://www.quanticol.eu/) 600708, and [ASCENS](http://www.ascens-ist.eu/) 257414.

[http://sysma.imtlucca.it/wp-content/uploads/2013/09/ascens_logo_new-300x50.png](http://www.ascens-ist.eu/)

We are grateful to the proposers of (P)VeStA, our starting point: Gul Agha, Musab Alturki, José Meseguer, Koushik Sen and Mahesh Viswanathan. 

Furthermore, we thank the main author of Alchemist (Danilo Pianini), who provided valuable help and suggestions to improve MultiVeStA, as well as Benjamin Byholm, who helped us in extending the support of MultiVeStA to python simulators. We also thank Stephen Gilmore and Mirco Tribastone, for their help in integrating MultiVeStA with BioPEPA. 

Last but not least, we thank Michele Amoretti and Alberto Lluch Lafuente, who supported and suggested this work from the very beginning.
