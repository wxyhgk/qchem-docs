---
title: "2.2.2 Integration with IQmol"
---

## 2.2.2 Integration with **IQmol**

(July 4, 2026)

## 2.2.2.1 Installation and Server Setup

**IQmol** provides a fully integrated molecular builder and viewer for the
**Q-Chem** package. It is available for the Windows, Linux, and Mac OS X
platforms and instructions for downloading and installing the latest version
can be found at `http://www.iqmol.org/downloads.html`.

**IQmol** can be run as a stand-alone package which is able to open existing
**Q-Chem** input/output files, but it can also be used as a fully functional
front end which is able to submit and monitor **Q-Chem** jobs, and to analyze the
resulting output. By default, **IQmol** submits **Q-Chem** jobs to a server that
is owned by **Q-Chem**, Inc., which provides prospective users with the
opportunity to run short **Q-Chem** demonstration jobs for free simply by
downloading **IQmol**, without the need to install **Q-Chem**.

For customers who own **Q-Chem**, it is necessary to configure **IQmol** to submit
jobs to an appropriate server. To do this, first ensure **Q-Chem** has been
correctly installed on the target machine and can be run from the command line.
Second, open **IQmol** and carry out the following steps:

1. 1.

Select the Calculation$\rightarrow$Edit Servers menu option. A dialog
will appear with a list of configured servers (which will initially be
empty).
2. 2.

Click the Add New Server button with the ‘+’ icon. This opens a dialog
which allows the new server to be configured. The server is the machine
which has your **Q-Chem** installation.
3. 3.

Give the server a name (this is simply used to identify the current
server configuration and does not have to match the actual machine name)
and select if the machine is local (*i.e.* the same machine as **IQmol** is
running on) or remote.
4. 4.

If there is PBS software running on the server, select the PBS ‘Type’
option, otherwise in most cases the Basic option should be sufficient.
Please note that the server must be Linux based and cannot be a Windows
server.
5. 5.

If required, the server can be further configured using the Configure
button. Details on this can be found in the embedded **IQmol** help which
can be accessed via the Help$\rightarrow$Show Help menu option.
6. 6.

For non-PBS servers the number of concurrent **Q-Chem** jobs can be limited
using a simple inbuilt queuing system. The maximum number of jobs is set
by the Job Limit control. If the Job Limit is set to zero the queue is
disabled and any number of jobs can be run concurrently. Please note
that this limit applies to the current **IQmol** session and does not
account for jobs submitted by other users or by other **IQmol** sessions.
7. 7.

The `$QC` environment variable should be entered in the given box.
8. 8.

For remote servers the address of the machine and your user name are also
required. **IQmol** uses SSH2 to connect to remote machines and the most
convenient way to set this up is by using authorized keys
(`)`
for details on how these can be set up). **IQmol** can then connect via
the SSH Agent and will not have to prompt you for your password. If you
are not able to use an SSH Agent, several other authentication methods
are offered:

- •

**Public Key** This requires you to enter your SSH passphrase (if
any) to unlock your private key file. The passphrase is stored in
memory, not disk, so you will need to re-enter this each time
**IQmol** is run.
- •

**Password Prompt** This requires each server password to be
entered each time **IQmol** is run. Once the connection has been
established the memory used to hold the password is overwritten to
reduce the risk of recovery from a core dump.

Further configuration of SSH options should not be required unless your
public/private keys are stored in a non-standard location.

It is recommended that you test the server configuration to ensure everything
is working before attempting to submit a job. Multiple servers can be
configured if you have access to more than one copy of **Q-Chem** or have
different account configurations. In this case the default server is the first
on the list and if you want to change this you should use the arrow buttons in
the Server List dialog. The list of configured servers will be displayed when
submitting **Q-Chem** jobs and you will be able to select the desired server for
each job.

Please note that while **Q-Chem** is file-based, as of version 2.1 **IQmol** uses
a directory to keep the various files from a calculation. More details can be
found in the **IQmol** `user manual`.

## 2.2.2.2 Reading **Q-Chem** Outputs

In addition to having IQmol communicate with **Q-Chem**, it can work standalone
by reading output files directly. A number of file formats are supported:

- •

**Q-Chem** outputs produced by running the *qchem* shell script
(Section [2.2.1](ssect_general-usage.md))
- •

Formatted checkpoint (`.fchk`) files: A formatted checkpoint file
can be requested by setting GUI = 2 in the *$rem* section of the
input, or equivalently by setting IQMOL_FCHK = TRUE. The
checkpoint file name is determined by the `$GUIFILE` environment
variable which by default is set to `${input}.fchk`.
- •

*qarchive* files: We have created a new file format designed to
overcome limitations of using text-based formats with post-processing and
visualization tools. The *qarchive* format is HDF5-based, supports
more of **Q-Chem**’s novel feature set than fchk files, and is tightly
integrated with **IQmol**. In order to create this file in your working
directory, pass the *-archive* flag to the *qchem* shell script and
add the following to the input:

> ```qchem
> $archive
>         enable_archive = True !Turns on generation of Archive
>     $end
> ```

The archive file is also always present in each job’s scratch directory when the *-save*
flag is used. It appears under the file name
`$QCSCRATCH/savename/qarchive.h5`
