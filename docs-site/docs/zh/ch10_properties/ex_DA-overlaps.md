---
title: "10.3.3 Donor–Acceptor Orbital Overlaps"
---

## 10.3.3 Donor–Acceptor Orbital Overlaps

(July 4, 2026)

In donor–acceptor (D–A) materials, the overlap between the donor orbital
(HOMO of D) and the acceptor orbital (LUMO of A) has been shown to correlate
with excited-state charge-transfer character.[[1337]](../bib_references/bib.md#bib1396)
 This overlap can be
computed, taking into account relaxation of the monomer geometries upon formation
of the D–A complex, using the *$rem* variable
MO_OVERLAPS_TWO_GEOMS, as shown in
Example 10.3.3 below. This requires two separate SCF calculations (one for
either D or A in isolation, and another for the dimer D–A), and both calculations must use
the same basis set. Therefore, ghost atoms should be added in the monomer calculation
so that both SCF calculations use the dimer basis set. Output is delivered in a directory
`OutputName.MO-overlaps` (where `OutputName` is the name of the **Q-Chem**
output file). This output consists of the $\alpha$-spin MO coefficients for both systems
(`CA-Geom1.txt` and `CA-Geom2.txt`), the AO overlap matrix between the
two calculations (`AO-overlap-TwoGeoms.txt`, which need not be an identity matrix
because the geometries could differ), and the MO overlap matrix between the two calculations
(`MO-overlap-TwoGeoms.txt`).

**Note: 

Currently, only overlaps between $\alpha$-spin MOs are considered, hence why only
$\alpha$-spin MO coefficients are returned. This means that this features is implemented
only for spin-restricted wave functions.
**

Alternatively, one might be interested in the degree of spatial overlap between donor and
acceptor orbitals (*e.g.*, HOMO and LUMO) within the same molecule or on two different molecules
within the same supramolecular calculation. These can be computed using the same tools that
are used to compute the $\Lambda$ metric in TDDFT [Eq. ([7.16](../ch07_excited/sec_CT-metrics.md#eq:Tozer-metric))], and the
contributing overlaps $O_{ia}$ [Eq. ([7.17](../ch07_excited/sec_CT-metrics.md#eq:Tozer-overlaps))] can be printed using
SPATIAL_OVERLAP_ANALYSIS. See Section [7.3.6.1](../ch07_excited/subsec_TDDFT-Control.md#subsec:TDDFT-Control:Basic)
for job control options and Example 10.3.3 for an example.

MO_OVERLAPS_TWO_GEOMS

### `MO_OVERLAPS_TWO_GEOMS`

> **Specifies whether to compute molecular orbital overlaps at two different geometries.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Do not compute these overlaps.
>     * 1
>     * Used to indicate the first of two required SCF calculations.
>     * 2
>     * Used to indicate the second of two required SCF calculations.
> * **Recommendation**: The atoms must be ordered in the same way for both calculations. (This is not checked.)

???+ example "Example 10.14: Compute “spatial overlaps” of the frontier MOs, for a dimer of naphthalene and tetracyanoquinone.
These are overlaps $O_{ia}$ of the absolute values
of the orbitals [ Eq. ( 7.17 )]. This feature is based on the $\Lambda$ metric
of TDDFT, therefore at least one excited state must be computed in order to trigger this analysis."
    ```qchem
    $molecule
    0 1
      C   1.262951   1.945976  -0.561360
      C   0.648393   2.896730   0.296837
      C   2.662678   1.710349  -0.545738
      H   3.283172   2.277769   0.142405
      C   3.225026   0.771942  -1.373626
      H   4.295659   0.593998  -1.345666
      C   2.415782   0.024414  -2.263235
      H   2.874995  -0.720497  -2.905219
      C   1.061881   0.234151  -2.304223
      H   0.435114  -0.339033  -2.982450
      C   0.449076   1.198213  -1.458953
      C  -0.950361   1.427044  -1.468096
      C  -1.241593  -0.113527   1.511623
      H  -1.776720   0.630886   2.090246
      C   0.087508  -0.255323   1.653805
      H   0.634524   0.372807   2.348013
      C   0.826509  -1.220978   0.861471
      C   2.186874  -1.336026   0.974224
      C   0.076113  -2.057065  -0.061488
      H   0.616720  -2.788316  -0.652909
      C  -1.255888  -1.926290  -0.191214
      H  -1.804801  -2.556542  -0.883200
      C  -1.987167  -0.926165   0.566999
      C  -3.333669  -0.739067   0.378968
      C  -1.516839   2.349538  -0.623777
      C  -0.708145   3.093806   0.267607
      H   1.274799   3.469589   0.975647
      H  -1.571143   0.856542  -2.154642
      H  -2.590617   2.512925  -0.634219
      H  -1.169539   3.821896   0.927541
      C   2.935702  -0.523467   1.883035
      C   2.933880  -2.256250   0.173594
      N   3.523004   0.145261   2.626355
      N   3.522832  -3.002457  -0.490547
      C  -4.043584   0.294041   1.066080
      C  -4.077033  -1.521605  -0.558360
      N  -4.657467  -2.163965  -1.330296
      N  -4.588038   1.154569   1.621873
    $end
    
    $rem
    method                wb97x-d
    basis                 6-31G*
    cis_triplets          false
    cis_n_roots           1    ! needed for spatial overlap analysis
    spatial_overlap_anal  true
    spatial_overlap_print 1
    $end
    ```

???+ example "Example 10.15: Compute MO overlaps for a C ${}_{\text{2}}$ H ${}_{\text{4}}\cdots$ C ${}_{\text{2}}$ F ${}_{\text{4}}$ dimer."
    ```qchem
    $comment
    Job 1: this is the dimer
    $end
    
    $molecule
    0 1
              C      -0.6656405432    -0.0000000000    -3.3601967383
              H      -1.2362909837    -0.9253767714    -3.3623091560
              H      -1.2362909837     0.9253767714    -3.3623091560
              C       0.6656405432     0.0000000000    -3.3601967383
              H       1.2362909837     0.9253767714    -3.3623091560
              H       1.2362909837    -0.9253767714    -3.3623091560
              C      -0.6610251661    -0.0000000000     1.1109504097
              F      -1.3861639022    -1.1014627457     1.1119323203
              F      -1.3861639022     1.1014627457     1.1119323203
              C       0.6610251661    -0.0000000000     1.1109504097
              F       1.3861639022     1.1014627457     1.1119323203
              F       1.3861639022    -1.1014627457     1.1119323203
    $end
    
    $rem
    method¯¯cam-b3lyp
    basis¯¯6-31+G*
    mo_overlaps_two_geoms 1 ! for job #1
    $end
    
    @@@
    
    $comment
    Job 2:  monomer1, with ghost functions for monomer2
    $end
    
    $molecule
    0 1
              C      -0.6656405432    -0.0000000000    -3.3601967383
              H      -1.2362909837    -0.9253767714    -3.3623091560
              H      -1.2362909837     0.9253767714    -3.3623091560
              C       0.6656405432     0.0000000000    -3.3601967383
              H       1.2362909837     0.9253767714    -3.3623091560
              H       1.2362909837    -0.9253767714    -3.3623091560
             @C      -0.6610251661    -0.0000000000     1.1109504097
             @F      -1.3861639022    -1.1014627457     1.1119323203
             @F      -1.3861639022     1.1014627457     1.1119323203
             @C       0.6610251661    -0.0000000000     1.1109504097
             @F       1.3861639022     1.1014627457     1.1119323203
             @F       1.3861639022    -1.1014627457     1.1119323203
    $end
    
    $rem
    method          cam-b3lyp
    basis           6-31+G*
    mo_overlaps_two_geoms 2 ! for job #2
    $end
    ```
