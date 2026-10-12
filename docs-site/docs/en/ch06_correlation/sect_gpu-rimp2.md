---
title: "6.6.4 GPU Implementation of RI-MP2"
---

## 6.6.4 GPU Implementation of RI-MP2

(July 4, 2026)

**Q-Chem** currently offers the possibility of accelerating RI-MP2 calculations
using graphics processing units (GPUs). Currently, this is implemented for
CUDA-enabled NVIDIA graphics cards only, such as (in historical order from
2008) the GeForce, Quadro, Tesla and Fermi cards. More information about
CUDA-enabled cards is available at

`http://www.nvidia.com/object/cuda_gpus.html`

It should be noted that these GPUs have specific power and motherboard
requirements.

Software requirements include the installation of the appropriate NVIDIA CUDA
driver (at least version 1.0, currently 3.2) and linear algebra library, CUBLAS
(at least version 1.0, currently 2.0). These can be downloaded jointly in
NVIDIA’s developer website:

`http://developer.nvidia.com/object/cuda_3_2_downloads.html`

We have implemented a mixed-precision algorithm in order to get *better than*
single precision when users only have single-precision GPUs. This is
accomplished by noting that RI-MP2 matrices have a *large* fraction of
numerically “small” elements and a *small* fraction of numerically
“large” ones. The latter can greatly affect the accuracy of the calculation
in single-precision only calculations, but calculation involves a relatively
small number of compute cycles. So, given a threshold value $\delta$, we
perform a separation between “small” and “large” elements and accelerate
the former compute-intensive operations using the GPU (in single-precision) and
compute the latter on the CPU (using double-precision). We are thus able to
determine how much double-precision we desire by tuning the $\delta$
parameter, and tailoring the balance between computational speed and accuracy.

### `CUDA_RI-MP2`

> **Enables GPU implementation of RI-MP2**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: GPU-enabled MGEMM off
>     * `TRUE`: GPU-enabled MGEMM on
> * **Recommendation**: Necessary to set to 1 in order to run GPU-enabled RI-MP2

### `USECUBLAS_THRESH`

> **Sets threshold of matrix size sent to GPU (smaller size not worth sending to GPU).**
>
> * **Type**: `INTEGER`
> * **Default**: `250`
> * **Options**:
>     * `n`: user-defined threshold
> * **Recommendation**: Use the default value. Anything less can seriously hinder the GPU acceleration

### `USE_MGEMM`

> **Use the mixed-precision matrix scheme (MGEMM) if you want to make calculations in your card in single-precision (or if you have a single-precision-only GPU), but leave some parts of the RI-MP2 calculation in double precision)**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: MGEMM disabled
>     * `TRUE`: MGEMM enabled
> * **Recommendation**: Use when having single-precision cards

### `MGEMM_THRESH`

> **Sets MGEMM threshold to determine the separation between “large” and “small” matrix elements. A larger threshold value will result in a value closer to the single-precision result. Note that the desired factor should be multiplied by 10000 to ensure an integer value.**
>
> * **Type**: `INTEGER`
> * **Default**: `10000`
> * **Options**:
>     * $n$: User-specified threshold
> * **Recommendation**: For small molecules and basis sets up to triple- $\zeta$ , the default value suffices to not deviate too much from the double-precision values. Care should be taken to reduce this number for larger molecules and also larger basis-sets.

???+ example "Example 6.6: RI-MP2 double-precision calculation"
    ```qchem
    $molecule
       0 1
       c
       h1  c  1.089665
       h2  c  1.089665  h1  109.47122063
       h3  c  1.089665  h1  109.47122063  h2   120.
       h4  c  1.089665  h1  109.47122063  h2  -120.
    $end
    
    $rem
       METHOD       rimp2
       BASIS        cc-pvdz
       AUX_BASIS    rimp2-cc-pvdz
       CUDA_RIMP2   1
    $end
    ```

???+ example "Example 6.7: RI-MP2 calculation with MGEMM"
    ```qchem
    $molecule
       0 1
       c
       h1  c  1.089665
       h2  c  1.089665  h1  109.47122063
       h3  c  1.089665  h1  109.47122063  h2   120.
       h4  c  1.089665  h1  109.47122063  h2  -120.
    $end
    
    $rem
       METHOD         rimp2
       BASIS          cc-pvdz
       AUX_BASIS      rimp2-cc-pvdz
       CUDA_RIMP2     1
       USE_MGEMM      1
       MGEMM_THRESH   10000
    $end
    ```
