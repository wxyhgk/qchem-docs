---
title: "2.1.5 User Account Adjustments"
---

## 2.1.5 User Account Adjustments

(July 4, 2026)

In order for individual users to run **Q-Chem**, User file access permissions
must be set correctly so that the user can read, write
and execute the necessary **Q-Chem** files. It may be advantageous to
create a *qchem* user group on your machine and recursively
change the group ownership of the **Q-Chem** directory to *qchem* group.

The **Q-Chem** run-time environment need to be initiated prior to running any **Q-Chem**
calculations, which is done by sourcing the environment setup script qcenv.sh (for bash) or
qcenv.csh (for csh and tcsh) placed in your **Q-Chem** top directory after a successful
installation. It might be more convenient for user to include the **Q-Chem** environment setup
in their shell startup script, *e.g.*, `.cshrc` or `.tcshrc` for csh or tcsh, respectively, or `.bashrc` for bash.

If using the csh or tcsh shell, add the following lines to the `.cshrc` file in the user’s home directory:

> ```qchem
> #
> setenv  QC         qchem_root_directory_name
> setenv  QCSCRATCH  scratch_directory_name
> source  $QC/qcenv.csh
> #
> ```

If using the Bourne-again shell (bash), add the following lines to the `.bashrc` file in the user’s home directory:

> ```qchem
> #
> export QC=qchem_root_directory_name
> export QCSCRATCH=scratch_directory_name
> . $QC/qcenv.sh
> #
> ```
