---
title: "6.17.3 Summary of Keywords"
---

## 6.17.3 Summary of Keywords

(July 4, 2026)

### `MEM_STATIC`

> **Sets the memory for individual Fortran program modules**
>
> * **Type**: `INTEGER`
> * **Default**: `240`
> * **Options**:
>     * $n$: User-defined number of megabytes.
> * **Recommendation**: For direct and semi-direct MP2 calculations, this must exceed OVN + requirements for AO integral evaluation (32–160 MB). Up to 2000 MB for large coupled-clusters calculations.

### `CC_MEMORY`

> **Specifies the maximum size, in MB, of the buffers for in-core storage of block-tensors in CCMAN and CCMAN2.**
>
> * **Type**: `INTEGER`
> * **Default**: `50% of`
> * **Options**:
>     * $n$: Integer number of MB
> * **Recommendation**: Larger values give better I/O performance and are recommended for systems with large memory (add to your .qchemrc file. When running CCMAN2 exclusively on a node, should be set to $\sim$ 80% of the total available RAM. )

### `CC_BACKEND`

> **Used to specify the computational back-end of CCMAN2.**
>
> * **Type**: `STRING`
> * **Default**: `VM`
> * **Options**:
>     * `XM`: libxm shared-memory disk-based back-end
>     * `INCORE`: in-core memory back-end
> * **Recommendation**: Use XM for large jobs with limited memory or when the performance of the default disk-based back-end is not satisfactory, INCORE for small jobs that fit in main memory.
