# Classical Simulations of Quantum Circuits Using Reinforcement Learning
<!-- ROADMAP -->
## Roadmap

- [x] design and implement the MPS-based simulation enviromnet  
- [x] design and implement the TTN-based simulation environment
- [x] Using RL algorithm to solve the MPS-based quantum circuits simulation problem
- [x] Using RL algorithm to solve the TTN-based quantum circuits simulation problem
- [ ] Design and implement the MPS-based massive parallel simulation envrionment
- [ ] Design and implement the TTN-based massive parallel simulation envrionment

## Result

## Experimental Results

|Form|N=10|N=30|N=50|N=100|
|-------| ----|------- | -----|------ |
|![TT](https://user-images.githubusercontent.com/75991833/217780619-40f42213-62b8-4db5-bfa9-0c9f8d97081d.png)|2464<br>2464<br>GAP：0%|2.1477512e9<br>2.14775169024e9<br>Gap: 2.283e-7|2.2518e15<br>2.2518001572826315e15<br>Gap: 6.985e-8|2.5353012e+30<br>2.535301200456459e+30<br>Gap: 1.8e-10|
|![TR](https://user-images.githubusercontent.com/75991833/217780649-80acaa33-030b-46b9-9fc6-bf5bc84167a3.png)|4864<br>4864<br>GAP：0.0%|4.2954993e9<br>4.29549879296e9<br>GAP：1.180e-7|4.5036e15<br>4.503600314565263e15<br>GAP：6.9e-8|5.0706024e+30<br>5.070602400912918e+30<br>GAP：1.8e-10|

|Form|N=7|N=15|N=31|N=63|N=127|
|-------| ----|------- | -----|------ |------ |
|![TTN](https://user-images.githubusercontent.com/75991833/217782955-cd2cd6e8-d0b8-4187-b7e7-d202266bcbfb.png)|30<br>30<br>GAP：0%|78<br>78<br>GAP：0%|174<br>180<br>GAP：3.45%|366<br>400<br>GAP：9.29%|750<br>832<br>GAP：10.94%|

|Form|N=9|N=16|N=49|N=81|N=100|
|-------| ----|------- | -----|------ |------ |
|![G](https://user-images.githubusercontent.com/75991833/217780858-eff2a41e-3847-4ed2-bbcb-5db8aa86d9ce.png)|1|2|3|4|5|

Reference:

[1] Meirom, E., Maron, H., Mannor, S., & Chechik, G. Optimizing tensor network contraction using reinforcement learning. In International Conference on Machine Learning (pp. 15278-15292). ICML 2022.
