_*MultiVeStA*_ is an efficient statistical analysis tool which can be easily integrated with existing discrete event simulators, enriching them with distributed Statistical Analysis and Statistical Model Checking capabilities.

The tool is maintained and developed by Stefano Sebastio and [Andrea Vandin](http://www.ecs.soton.ac.uk/people/av1v13). The tool comes as an extension of the existing VeStA and PVeStA tools, developed at the Department of Computer Science at the University of Illinois at Urbana-Champaign.

The currently supported discrete event simulators are (in alphabetic order):
   * [http://apice.unibo.it/xwiki/bin/view/Alchemist/ Alchemist]: _a simulator targeting chemical-oriented computational systems_
   * [http://iridia.ulb.ac.be/argos/ ARGoS]: _a multi-robot, multi-engine simulator for heterogeneous Swarm robotics_ 
   * [http://www.biopepa.org/ Bio-PEPA]: _a language for the modelling and the analysis of biochemical networks_
   * [http://code.google.com/p/deus/ DEUS]: _a general-purpose, open-source, simulator for the analysis of large scale systems_
   * [https://code.google.com/p/multivesta/wiki/QFLan QFLan]: _a probabilistic feature-oriented language with quantitative constraints for product families_
   * [http://sysma.lab.imtlucca.it/misscel/ MISSCEL]: _an interpreter and simulator for the Service Component Ensemble Language_
   * Any python simulator, resorting to [http://py4j.sourceforge.net/ Py4J]
   * [http://www.sciencedirect.com/science/article/pii/S1571066106002672 Probabilistic Maude]: _an engine to execute probabilistic rewrite theories_
   * A built in DTMC and CTMC engine




   * _other simulators coming soon_
   * _*...and yours with just few lines of code*_ (just [mailto:a.vandin@soton.ac.uk;stefano.sebastio@imtlucca.it contact us!]).


Download [https://docs.google.com/file/d/0B1wH4SBkfGwYUklocFMtSWlIMkU/edit?usp=sharing MultiVeStA], and check the [http://code.google.com/p/multivesta/w/list Wiki page] of this site for guidelines on using it (or just [mailto:andrea.vandin@imtlucca.it;stefano.sebastio@imtlucca.it contact us!]).

== Papers ==
   * [http://dl.acm.org/citation.cfm?id=2631884 MultiVeStA: Statistical Model Checking for Discrete Event Simulators] (*please cite this work*) in the proceedings of _VALUETOOLS'13_ ([http://eprints.imtlucca.it/1798/ extended version])
   * [https://www.dropbox.com/s/qty17idt76lbaie/SPLC15.pdf?dl=0 Statistical Analysis of Probabilistic Models of Software Product Lines with Quantitative Constraints] in the proceedings of _  SPLC'15 _
   * [http://arxiv.org/ct?url=http%3A%2F%2Fdx.doi.org%2F10%252E4204%2FEPTCS%252E182%252E5&v=3359e1fe Quantitative Analysis of Probabilistic Models of Software Product Lines with Statistical Model Checking] in the proceedings of _  FMSPLE'15 _
   * [http://link.springer.com/chapter/10.1007%2F978-3-319-10181-1_5 An Analysis Pathway for the Quantitative Evaluation of Public Transport Systems]  in the proceedings of _  IFM'14 _
   * [http://eprints.imtlucca.it/1697/ Distributed statistical analysis of complex systems modeled through a chemical metaphor]  in the proceedings of _  HPCS'14 _
   * [http://link.springer.com/chapter/10.1007%2F978-3-642-54624-2_10 Reasoning (on) Service Component Ensembles in Rewriting Logic] in the proceedings of _  SAS'14 _
   * [http://dx.doi.org/10.1145/2593929.2593943 A Computational Field Framework for Collaborative Task Execution in Volunteer Clouds] in the proceedings of _ SEAMS'14 _
   * [http://dx.doi.org/10.1007/978-3-662-43813-8_15 Reputation-based Cooperation in the Clouds] in the proceedings of _ IFIPTM'14 _


   

== Other Related Papers ==   
   * [http://www.computer.org/csdl/proceedings/qest/2005/2427/00/24270251-abs.html VESTA: A Statistical Model-checker and Analyzer for Probabilistic Systems]
   * [http://link.springer.com/chapter/10.1007%2F978-3-642-22944-2_28 PVeStA: A Parallel Statistical Model Checking and Quantitative Analysis Tool]
   * [http://www.sciencedirect.com/science/article/pii/S1571066106002672 PMaude: Rewrite-based Specification Language for Probabilistic Object Systems]


== Acknowledgments ==
Our work is developed within and supported by the European projects [http://www.quanticol.eu/ QUANTICOL] 600708, and [http://www.ascens-ist.eu/ ASCENS] 257414.

[http://www.ascens-ist.eu/ http://sysma.imtlucca.it/wp-content/uploads/2013/09/ascens_logo_new-300x50.png]

We are grateful to the proposers of (P)VeStA, our starting point: Gul Agha, Musab Alturki, José Meseguer, Koushik Sen and Mahesh Viswanathan. 

Furthermore, we thank the main author of Alchemist (Danilo Pianini), who provided valuable help and suggestions to improve MultiVeStA, as well as Benjamin Byholm, who helped us in extending the support of MultiVeStA to python simulators. We also thank Stephen Gilmore and Mirco Tribastone, for their help in integrating MultiVeStA with BioPEPA. 

Last but not least, we thank Michele Amoretti and Alberto Lluch Lafuente, who supported and suggested this work from the very beginning.
