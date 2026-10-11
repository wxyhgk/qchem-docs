---
title: "2.1.4 Q-Chem Run-time Environment Variables"
---

## 2.1.4 **Q-Chem** Run-time Environment Variables

(July 4, 2026)

**Q-Chem** requires the following shell environment variables setup prior to running any
calculations:

| QC | Defines the location of the Q-Chem directory structure. The qchem.install shell script determines this automatically. |
| --- | --- |
| QCAUX | Defines the location of the auxiliary information required by Q-Chem , which includes the license required to run Q-Chem . If not explicitly set by the user, this defaults to $QC/qcaux . |
| QCSCRATCH | Defines the directory in which Q-Chem will store temporary files. Q-Chem will usually remove these files on successful completion of the job, but they can be saved, if so wished. Therefore, $QCSCRATCH should not reside in a directory that will be automatically removed at the end of a job, if the files are to be kept for further calculations. Note that many of these files can be very large, and it should be ensured that the volume that contains this directory has sufficient disk space available. The $QCSCRATCH directory should be periodically checked for scratch files remaining from abnormally terminated jobs. $QCSCRATCH defaults to the working directory if not explicitly set. Please see section 2.2 for details on saving temporary files and consult your systems administrator. |
| QCLOCALSCR | On certain platforms, such as Linux clusters, it is sometimes preferable to write the temporary files to a disk local to the node. $QCLOCALSCR specifies this directory. The temporary files will be copied to $QCSCRATCH at the end of the job, unless the job is terminated abnormally. In such cases Q-Chem will attempt to remove the files in $QCLOCALSCR , but may not be able to due to access restrictions. Please specify this variable only if required. |
