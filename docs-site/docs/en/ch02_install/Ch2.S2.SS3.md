---
title: "2.2.3 Customizable Archive Files"
---

## 2.2.3 Customizable Archive Files

(July 4, 2026)

**Q-Chem** supports a customizable archive file which permits the saving of
various data from the calculation. The contents of the archive is controlled
via data keywords specified in the *$schema* section of the input file. The
format of the schema is in YAML and currently the level of indentation must be
exactly 2 spaces.

The following data keywords are valid within the *$schema* section:

| ApproxHessian | ContractionCoefficients | Coordinates |
| --- | --- | --- |
| DensityMatrix | Energy | FockMatrix |
| Gradient | NAlpha | NBeta |
| Nuclei | OrbitalCoefficients | OrbitalEnergies |
| OrthonormalizationMatrix | OverlapMatrix | PrimitiveExponents |
| PrimitivesPerShell | ShellCoordinates | ShellToAtomMap |
| ShellTypes | SpContractionCoefficients | TotalCharge |

Data can be nested allowing, for example, not just the final MO coefficients to
be printed, but those for each cycle of the SCF as well.
The following container levels are available and are used to control this level
of nesting:

| BasisSet | GeomOpt | GeomOptStep |
| --- | --- | --- |
| SCF | SCFStep | Structure |

The archive is written to `$QCSCRATCH/savename/qch5_archive.h5` and the contents
can be accessed using standard HDF5 tools.

???+ example "Example 2.2: Sample input showing a custom schema specification for the archive file
in the $schema section. In the first job the SCF data have been nested
which requests the MO coefficients to be printed on each cycle. In the
second job, basis set data similar to those in the formatted checkpoint
file have been requested."
    ```qchem
    $molecule
    0 1
    C          0.00000       -0.00000       -0.68020
    C         -0.00000        0.00000        0.68020
    H         -0.00000       -0.89374       -1.19620
    H          0.00000        0.89374       -1.19620
    H         -0.00000       -0.89374        1.19620
    H          0.00000        0.89374        1.19620
    $end
    
    $rem
      JOBTYPE  opt
      METHOD   hf
      BASIS    sto-3g
    $end
    
    $schema
    GeomOpt
      GeomOptStep
        SCF
          Energy
          OrbitalCoefficients
    $end
    
    @@@
    
    $molecule
      read
    $end
    
    $rem
      METHOD    hf
      BASIS     sto-3g
    $end
    
    $schema
    SCF
      Energy
      FockMatrix
      DensityMatrix
      OrbitalCoefficients
    BasisSet
      ShellTypes
      ShellToAtomMap
      ShellCoordinates
      PrimitivesPerShell
      PrimitiveExponents
      ContractionCoefficients
      SpContractionCoefficients
    $end
    
    
    ```
