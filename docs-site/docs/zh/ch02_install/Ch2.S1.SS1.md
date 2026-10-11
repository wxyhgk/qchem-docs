---
title: "2.1.1 Downloading and Licensing"
---

## 2.1.1 Downloading and Licensing

(July 4, 2026)

Users are referred to the detailed installation instructions available at
`https://www.q-chem.com/install/`.

An encrypted license file must be obtained from your vendor before you will be
able to use **Q-Chem**. Q-Chem licenses can be issued in one of two ways.
In the first method, node-locked licensing, **Q-Chem** will only operate correctly
on the machine for which the license file(s) have been generated.
In the second method, FlexNet licensing, the license is issued for one node,
and the other nodes check out licenses in order to run Q-Chem.
These licensing types are described in further detail below, and information
about obtaining these files can be found in the installation section.

**Do not alter the license file unless directed by **Q-Chem**, Inc.**

## 2.1.1.1 Node-locked Licensing

Node-locked licensing requires obtaining a license for each machine that will
be running **Q-Chem**. On a supercomputing cluster, for example, host IDs need
to be generated for each individual node, and the license file must be
regenerated whenever nodes are added or removed from the cluster.
This licensing option works best for running Q-Chem on workstations, and in
some special cases where FlexNet licensing is untenable.

## 2.1.1.2 FlexNet Licensing

FlexNet (formerly known as flexlm) is a convenient option for managing Q-Chem
licenses in a computer cluster or supercomputer setting. One node (for example,
the head node in a cluster or another dedicated node) runs the licensing server
software and provides access to the Q-Chem license to all client compute nodes.
This method requires coordination with the administrator of the cluster to set up,
but information only needs to be collected for one node, and you can easily add or
remove nodes from the cluster without needing to reissue the license.
The FlexNet server licensing option is available free of charge to eligible
users running Q-Chem for Linux.
