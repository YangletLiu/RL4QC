# Classical Simulations of Quantum Circuits Using Reinforcement Learning
<!-- ROADMAP -->
## Roadmap
- [ ] design and implement the MPS-based simulation enviromnet (Gym style)
- [ ] design and implement the TTN-based simulation environment (Gym style)
- [ ] Using RL algorithm to solve the MPS-based quantum circuits simulation problem
- [ ] Using RL algorithm to solve the TTN-based quantum circuits simulation problem
- [ ] Dataset and benchmark
- [ ] Design and implement the MPS-based massive parallel simulation envrionment
- [ ] Design and implement the TTN-based massive parallel simulation envrionment


## Experimental Results
### Tensor-Train/MPS tensor network  
![TT](https://user-images.githubusercontent.com/75991833/217780619-40f42213-62b8-4db5-bfa9-0c9f8d97081d.png)  



File structure:    
mps\     
————baseline\  
————————————init.py, cotengra.py, opt_einsum.py      
————dataset_generation\   
————————————init.py, mps_generate.py       



To run the baseline methods, just execute ___"python  cotengra.py"___ or ___"python opt_einsum.py"___, where the variable ___n___ is the number of the tensor network.    
To generate the Tensor-Train/MPS dataset, please execute ___"python mps_generate.py"___, where the variable ___V___ in the ___main___  part is the number of tensor nodes.       

We present the ___Number of multiplications___ versus the ___Number of tensor nodes___ in the tensor-train/mps tensor network in the following table,    

| number of nodes | 10    | 50     | 100    | 200    | 400     | 600     | 800     | 1000    | 1500    | 2000    |    
|-----------------|-------|--------|--------|--------|---------|---------|---------|---------|---------|---------|  
| OE greedy       | 3.848 | 15.875 | 30.927 | 61.030 | 121.236 | 181.442 | 241.648 | 301.854 | X       | X       |  
| OE dynamic      | 3.693 |-------|-------|-------|--------|--------|--------|--------|--------|--------|  
| CTG greedy      | 3.693 | 15.656 | 30.705 | 60.808 | 121.014 | 181.220 | 241.426 | 301.632 | X       | X       |  
| CTG kahypar     | 3.690 | 15.650 | 30.710 | 60.810 | 121.010 | 181.220 | 241.430 | 301.630 | 451.150 | 602.660 |  
| RL-Hamiltonian  |       |        |        |        |         |         |         |         |         |         |  

note: (1) OE dynamic can not give a solution in a limited time for the number of nodes from 50 to 2000.  
(2) OE greedy and CTG greedy can not scale up to the number of nodes 15000 and 2000.  


### Sycamore circuit    

File structure:    
mps\     
————baseline\  
————————————init.py, cotengra.py, opt_einsum.py      
————dataset\          

We present the ___Number of multiplications___ versus the ___Number of cycles___ in the sycamore circuit in the following table,    
| number of cycles| 12    | 14     | 16     | 18     | 20      |      
|-----------------|-------|--------|--------|--------|---------|  
| OE greedy       | 17.795| 19.679 | 25.889 | 26.793 | 26.491 |  
| OE dynamic      | ------- |------- |------- |------- |-------- |   
| CTG greedy      | 17.065 | 19.282 | 23.151 | 23.570 | 25.623 |    
| CTG kahypar     | 13.408 | 14.152 | 17.012 | 17.684 | 18.826 |     
| RL-Hamiltonian  |       |        |        |        |         |      


Reference:

[1] Meirom, E., Maron, H., Mannor, S., & Chechik, G. Optimizing tensor network contraction using reinforcement learning. In International Conference on Machine Learning (pp. 15278-15292). ICML 2022.  
[2] Daniel, G., Gray, J., et al. (2018). Opt_einsum-a python package for optimizing contraction order for einsum-like expressions. Journal of Open Source Software, 3(26):753 https://github.com/dgasmith/opt_einsum
[3] Gray, J. and Kourtis, S. (2021). Hyper-optimized tensor network contraction. Quantum, 5:410. https://github.com/jcmgray/cotengra 
