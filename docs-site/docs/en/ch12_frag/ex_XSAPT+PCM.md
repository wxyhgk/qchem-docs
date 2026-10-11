---
title: "12.10.4 Running an XSAPT+MBD Job"
---

## 12.10.4 Running an XSAPT+MBD Job

(July 4, 2026)

In order to run an XSAPT job, at least two separate jobs must be run, a third
is optional and suggested in the case where the induction energy is thought to be important.
The first job that must be run is a second-order SAPT job without charge embedding on the full system.
This job provides the value for the electrostatic term, the exchange term, and the dispersion term.
(For an XSAPT+MBD method[[200]](../bib_references/bib.md#bib188)
 job, the dispersion value will
be the dispersion value obtained from the MBD calculation).
The second job that needs to be run is a SAPT job with charge embedding on the full system.
This SAPT job with charge embedding acts as a correction for the induction energy
and must be run on each pair of monomers.
The final induction energy for an XSAPT job is then the induction energy from
the SAPT job without charge embedding plus the difference between the total SAPT
energy with charge embedding minus the total SAPT energy without charge embedding.
In equation form, the XSAPT contribution to the induction energy would be:

<a id="eq:xsapt_pol"></a>

$$
E_{\text{pol}}=\sum_{A}\sum_{B>A}\left[E_{AB}^{\text{XSAPT}}(AB)-E_{AB}^{\text{SAPT}}\right] \tag{12.69}
$$

Here the term in brackets is the difference between the charge-embedded energy for the $AB$
dimer and the SAPT energy computed without charge embedding.
Therefore, the electrostatic, exchange, and dispersion energy would be the equivalent
to the same terms calculated from a normal SAPT calculation, it is the induction
energy that changes upon an XSAPT calculation.
An additional calculation can be performed to further correct the induction energy,
this is the $\delta$HF calculation, which accounts for higher than second-order induction energy.
The resulting delta(SCF) energy term is then added to the induction energy term
calculated as described above.

The above procedure is the required procedure for performing an XSAPT ($+\delta$HF)
calculation on a dimer complex.
In order to perform an XAPT ($+\delta$HF) calculation on an n-mer complex, several
more calculations need to be performed.
The first of which is to run a SAPT job with charge embedding on each pair of monomers.
This is required because the polarization of the dimers differs from that of the
dimers embedded in the charges of the entire system.
The second set of jobs, if the $\delta$HF correction is being performed, is
a $\delta$HF job on every pair of monomers.
These sets of jobs will again provide a correction to the induction energy for the system.

Two scripts to help the user perform an XSAPT+MBD+$\delta$HF calculation exist in
the `$QC/bin/tools` directory.
The script named `xsapt_creation.py` creates three files for an arbitrary
geometry (defined by the user), a SAPT job without embedding, a SAPT job with
embedding, and a $\delta$HF job.
See the script for instructions on how to use and modify the script for
personal use.
The other script named `xsapt_data_collection.py` looks through the
output files of the three jobs created by `xsapt_creation.py` and
performs the needed arithmetic to obtain the correct energy decomposition for
an XSAPT+MBD+$\delta$HF job.
See the script for instructions on how to use and modify it for personal use.

???+ example "Example 12.42: AO-XSAPT(KS)+ ai D3 calculation of water-water interaction."
    ```qchem
    $molecule
    0 1
    --
       0 1
       O  -1.551007  -0.114520   0.000000
       H  -1.934259   0.762503   0.000000
       H  -0.599677   0.040712   0.000000
    --
       0 1
       O   1.350625   0.111469   0.000000
       H   1.680398  -0.373741  -0.758561
       H   1.680398  -0.373741   0.758561
    $end
    
    $rem
       JOBTYPE            xsapt
       EXCHANGE           gen
       LRC_DFT            true ! add LR-HFX
       BASIS              aug-cc-pVTZ
       MEM_TOTAL          46000
       MEM_STATIC         4000
       AO2MO_DISK         35000
       CHELPG_DX          5
       CHELPG_HEAD        30
       CHELPG_H           110
       CHELPG_HA          590
    $end
    
    $xpol
       embed   charges
       charges CHELPG
       DFT-LRC
       print   3
    $end
    
    $sapt
       algorithm     ao  ! for use with +aiD dispersion
       order         2   ! 2nd-order SAPT
       basis         projected
       Dispersion    aiD3
       print         3
    $end
    
    $xc_functional
       x   wPBE  1.0
       c   PBE   1.0
    $end
    
    $lrc_omega
       502
       502
    $end
    ```

???+ example "Example 12.43: XSAPT+MBD with PCM boundary conditions."
    ```qchem
    $molecule
    0 1
    --
    0 1
    C    0.780147171  -0.609914733  -1.207556891
    H    0.896191595  -1.137639594  -2.144144625
    C    0.477942753   0.750993631  -1.207895407
    H    0.356964231   1.278167803  -2.144054074
    C    0.327289279   1.431867868  -0.000000000
    H    0.091465028   2.487139215   0.000000000
    C    0.477942754   0.750993631   1.207895407
    H    0.356964231   1.278167803   2.144054074
    C    0.780147171  -0.609914733   1.207556891
    H    0.896191595  -1.137639594   2.144144625
    C    0.931648311  -1.289981342   0.000000000
    H    1.168485730  -2.345213690  -0.000000000
    --
    0 1
    O   -2.743831210  -0.269262567   0.000000000
    H   -2.579027215  -1.213984095   0.000000000
    H   -1.856530267   0.102327758   0.000000000
    $end
    
    $rem
    jobtype ¯xsapt
    basis ¯¯def2-svpd
    lrc_dft ¯true
    method ¯¯lrc-wpbe
    scf_convergence 8
    solvent_method ¯pcm
    $end
    
    $xpol
    embed none
    dft-lrc
    print 3
    $end
    
    $sapt
    algorithm ao
    basis projected
    order 2
    print 3
    dispersion mbd
    $end
    
    $lrc_omega
    341
    502
    $end
    ```

???+ example "Example 12.44: XSAPT+oC8(r)aimMBD for the Hg $\cdots$ H ${}_{2}$ O van der Waals complex."
    ```qchem
    $comment
      XSAPT+oC8(r)aimMBD for the Hg...H2O van der Waals complex.
      def2-TZVPD auto-loads the matching ECP for Z > 36 (Hg), so the
      relativistic (r)aim free-atom reference is engaged automatically.
    $end
    
    $molecule
    0 1
    --
    0 1
       Hg    0.00000   0.00000   0.00000
    --
    0 1
       O     0.00000   0.00000   3.50000
       H     0.75670   0.00000   4.08590
       H    -0.75670   0.00000   4.08590
    $end
    
    $rem
       jobtype          xsapt
       method           hf
       basis            def2-tzvpd
       symmetry         false
       sym_ignore       true
       no_reorient      true
       scf_algorithm    diis
       scf_convergence  8
       mem_total        16000
       mem_static       8000
    $end
    
    $xpol
       embed none
       print 3            ! report per-atom Hirshfeld volume ratios
    $end
    
    $sapt
       algorithm  ao
       Dispersion OC8RAIMMBD   ! select the relativistic many-body AIM dispersion
    $end
    ```
