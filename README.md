# Classical Simulations of Quantum Circuits Using Reinforcement Learning
<!-- ROADMAP -->   

## :pencil: Foreword   

__Who wins in the classical versus quantum computing competition ?__ :open_mouth:    
Back in 2019, Google proudly announced “quantum supremacy” with its 53-qubit Sycomore quantum circuits,  which was later challenged by researchers claiming to have pulled ahead of Google on classical computers. We assert that any tech giant, university spinoff, or startup is too hasty to advertise ``quantum supremacy” via quantum circuits on the scale of 50 ～ 100 qubits.  
Thus, __an improved benchmark curve :chart_with_upwards_trend: for classical simulations for quantum circuits__ is really important. This is also the reason why we start this project.    

## :dart: Our goal  

By representing the quantum gates as the tensor diagrams, the quantum circuits can be represented by a tensor network. The simulation of the quantum circuit involves contracting the tensor network in a specific order. To improve the efficiency of classical simulations of quantum circuits, we need to find a better contraction order with fewer multiplications.  

One potential solution is to use reinforcement learning (RL) algorithms, which have shown promise in solving similar combination problems like graph cut and TSP. Some researchers have proposed using RL to find the optimal tensor network contraction order, but this alone may not be enough to accurately measure "quantum supremacy" and improve the benchmark curve.      

__We hope this project can bridge the gap between the quantum circuit and the deep learning, especially the RL community, to work together to find the real “quantum supremacy” . Come and join us in our mission to unlock the full potential of quantum circuits and revolutionize the world of computing!__  :raised_hands:


## :triangular_flag_on_post: Roadmap  

In our project, we will mainly focus on three aspects, namely the dataset, simulation envrionment, and benchmark,

__Dataset__: We will release various datasets for the tensor representations of quantum circuits, for other researchers to verify their ideas.  
:white_check_mark: Tensor-Train/MPS tensor network  
:white_check_mark: Tensor-Ring tensor network  
:white_check_mark: Tree tensor network  
:white_large_square: PEPS tensor network  
:white_large_square: MERA tensor network  
:white_large_square: Google's Sycamore circuit  

__Simulation environment__: We will develop efficient simulation environments for reserchers to debug their algirithms. For each tensor network, we will develop the single and the parallel version of the simulation environment, respectively. The parallel enviroment will be much more efficient in the data sampling, thus to significantly improve the efficiency of training RL agents.  

|Tensor network| Single :bike: | Parallel :rocket:|   
|-----------------|-------|--------|  
|TT/MPS|:white_large_square:|:white_large_square:|  
|TR|:white_large_square:|:white_large_square:|  
|Tree|:white_large_square:|:white_large_square:|  
|PEPS|:white_large_square:|:white_large_square:|  
|MERA |:white_large_square:|:white_large_square:|  
|Sycamore|:white_large_square:|:white_large_square:|    


__Benchmark__: We will merge and supply widely used algorithms, which has been applied for the classical simulations of quantum circuits, for other researchers to compare their methods' performance.  
:white_check_mark: greey strategy of optimized einsum (OE greedy)  
:white_check_mark: dinamic programming of optimized einsum (OE dynamic)  
:white_check_mark: cotengra kahypar (CTG kahypar)      
:white_check_mark: cotengra greedy (CTG greedy)  
:white_large_square: RL-Hamiltonian      

:wave: We are always welcome other researchers to contribute the benchmark algorithms, including the suggestions of methods, better hyper-parameters, etc., and the datasets, especially the pratical quantum circuits.   




## :clipboard: Experimental Results  

### File Structure

```
RL4QuantumCircuits
├── baseline
|    ├──mps
|    |──tr
|    |──tree
|    |──peps
|    |──mera
|    |──sycamore
├── datasets_generator
|    ├──mps
|    |──sycamore
|    |──tr
|    |──tree
|    |──peps
├── simulation_data
|    ├──mps
|    |──sycamore
|    |──tr
|    |──tree
|    |──peps
├── rl
|    ├──mps
|    ├──sycamore
├── verification
|    ├──code
|    ├──orders
```

We provide the classical simulation data of quantum circuits in the __simulation_data__ dictionary, which covers the Sycamore circuits,  matrix product state (mps), tensor ring (tr), tensor tree (tree), and peps with a range of nodes.  
In each file, we use the string to represent the quantum circuits, where each character stands for an edge, and the adjacent character indicates the connections between nodes.  



### How to run   
:small_orange_diamond: To run the baseline methods, just execute ___"python  cotengra.py"___ or ___"python opt_einsum.py"___, where the variable n is the number of the tensor nodes.      
:small_orange_diamond: To generate the  dataset, please execute __"python *_generate.py"___, where the variable V in the main  part is the number of tensor nodes.        

### Tensor-Train/MPS tensor network   

We present the ___Number of multiplications___ versus the ___Number of tensor nodes___ in the tensor-train/mps tensor network in the following table,    

| number of nodes | 10    | 50     | 100    | 200    | 400     | 600     | 800     | 1000    | 1500    | 2000    |    
|-----------------|-------|--------|--------|--------|---------|---------|---------|---------|---------|---------|  
| OE greedy       | 3.848 | 15.875 | 30.927 | 61.030 | 121.236 | 181.442 | 241.648 | 301.854 | X       | X       |  
| CTG greedy      | 3.693 | 15.656 | 30.705 | 60.808 | 121.014 | 181.220 | 241.426 | 301.632 | X       | X       |  
| CTG kahypar     | 3.690 | 15.650 | 30.710 | 60.810 | 121.010 | 181.220 | 241.430 | 301.630 | 451.150 | 602.660 |  
| RL-Hamiltonian  | 3.392 | 15.232 | 30.404 | 60.507 | 120.713 | 180.919 | 241.125 | 301.331 |         |         |  

:warning: Note:   
(1) OE dynamic can not give a solution in a limited time for the number of nodes from 50 to 2000.  
(2) OE greedy and CTG greedy can not scale up to the number of nodes 1500 and 2000.  


### Sycamore circuit          


We present the ___Number of multiplications___ versus the ___Number of cycles___ in the sycamore circuit in the following table,    
| number of cycles| 12    | 14     | 16     | 18     | 20      |      
|-----------------|-------|--------|--------|--------|---------|  
| OE greedy       | 17.795| 19.679 | 25.889 | 26.793 | 26.491 |   
| CTG greedy      | 17.065 | 19.282 | 23.151 | 23.570 | 25.623 |    
| CTG kahypar     | 13.408 | 14.152 | 17.012 | 17.684 | 18.826 |     
| RL-Hamiltonian  |       |        |        |        |         |      


### Related blogs  
About tensor networks https://zhuanlan.zhihu.com/p/623285707   
About tensor-train/mps tensor network  https://zhuanlan.zhihu.com/p/623582170   
About quantum circuits simulations using tensor networks https://zhuanlan.zhihu.com/p/624353259  
About the design of environments https://zhuanlan.zhihu.com/p/627658313  
About the tensor network dataset generation https://zhuanlan.zhihu.com/p/628239428?  

### Reference:

[1] Meirom, E., Maron, H., Mannor, S., & Chechik, G. Optimizing tensor network contraction using reinforcement learning. In International Conference on Machine Learning (pp. 15278-15292). ICML 2022.  
[2] Daniel, G., Gray, J., et al. (2018). Opt_einsum-a python package for optimizing contraction order for einsum-like expressions. Journal of Open Source Software, 3(26):753 https://github.com/dgasmith/opt_einsum    
[3] Gray, J. and Kourtis, S. (2021). Hyper-optimized tensor network contraction. Quantum, 5:410. https://github.com/jcmgray/cotengra    
  
