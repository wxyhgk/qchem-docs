---
title: "10.5.4 Generation of Volumetric Data Using $plots"
---

## 10.5.4 Generation of Volumetric Data Using *$plots*

(July 4, 2026)

The simplest way to visualize the charge densities and molecular orbitals that
**Q-Chem** evaluates is via a graphical user interface, such as those described
in the preceding section. An alternative procedure, which is often useful for
generating high-quality images for publication, is to evaluate certain
densities and orbitals on a user-specified grid of points. This is
accomplished by invoking the *$plots* option, which is itself enabled by
requesting IANLTY = 200.

The format of the *$plots* input is documented below. It permits plotting of
molecular orbitals, the SCF ground-state density, and excited-state densities
obtained from CIS, RPA or TDDFT/TDA, or TDDFT calculations. Also in connection
with excited states, either transition densities, attachment/detachment
densities, or natural transition orbitals (at the same levels of theory given
above) can be plotted as well. See Ref. [[572]](../bib_references/bib.md#bib586)
 for descriptions
of these various possibilities.
Please note that plotting complex-valued orbitals and electron densities from
Complex-Absorbing-Potential Hartree-Fock calculations is so far only possible
by direct generation of cube files (see Section [10.5.5](sec_cubefiles.md)).

By default, the output from the *$plots* command is one (or several) plain text
files in the working directory, named `plot.mo`, *etc.*. The results
then must be visualized with a third-party program capable of making
3-D plots. (Some suggestions are given in Section [10.5.5](sec_cubefiles.md).)

An example of the use of the *$plots* option is the following input deck:

???+ example "Example 10.24: A job that evaluates the H ${}_{2}$ HOMO and LUMO on a $1\times 1\times 15$ grid,
along the bond axis. The plotting output is in an ASCII file called plot.mo , which lists for each grid point, $x$ , $y$ , $z$ , and the value
of each requested MO."
    ```qchem
    $molecule
       0  1
       H   0.0   0.0   0.35
       H   0.0   0.0  -0.35
    $end
    
    $rem
       METHOD     hf
       BASIS      6-31g**
       IANLTY     200
    $end
    
    $plots
       Plot the HOMO and the LUMO on a line
       1   0.0   0.0
       1   0.0   0.0
      15  -3.0   3.0
       2   0   0   0
       1   2
    $end
    ```

General format for the *$plots* section of the **Q-Chem** input deck.

> *$plots*
> 
> 
>         One comment line 
> 
> 
>         Specification of the 3-D mesh of points on 3 lines: 
> 
> 
>                $N_{x}\quad x_{\mathrm{min}}\quad x_{\mathrm{max}}$ 
> 
> 
>                $N_{y}\quad y_{\mathrm{min}}\quad y_{\mathrm{max}}$ 
> 
> 
>                $N_{z}\quad z_{\mathrm{min}}\quad z_{\mathrm{max}}$ 
> 
> 
>         A line with 4 integers indicating how many things to plot: 
> 
> 
>                $N_{\mathrm{MO}}\quad N_{\mathrm{Rho}}\quad N_{\mathrm{Trans}}\quad N_{\mathrm{DA}}$ 
> 
> 
>         An optional line with the integer list of MO’s to evaluate
> (only if $N_{\mathrm{MO}}>0$)
> 
> 
>                MO(1)  MO(2) $\ldots$ MO($N_{\mathrm{MO}}$) 
> 
> 
>         An optional line with the integer list of densities to evaluate
> (only if $N_{\mathrm{Rho}}>0$) 
> 
> 
>                Rho(1)  Rho(2) $\ldots$ Rho($N_{\mathrm{Rho}}$) 
> 
> 
>         An optional line with the integer list of transition densities
> (only if $N_{\mathrm{Trans}}>0$) 
> 
> 
>                Trans(1)  Trans(2) $\ldots$ Trans($N_{\mathrm{Trans}}$) 
> 
> 
>         An optional line with states for detachment/attachment densities
> (if $N_{\mathrm{DA}}>0$) 
> 
> 
>                DA(1)  DA(2) $\ldots$ DA($N_{\mathrm{DA}}$) 
> 
> 
> *$end*

Line 1 of the *$plots* keyword section is reserved for comments. Lines 2–4
list the number of one dimension points and the range of the grid (note that
coordinate ranges are in Ångstroms if INPUT_BOHR is not set,
while all output is in atomic units). Line 5 must contain 4 non-negative
integers indicating the number of: molecular orbitals ($N_{\mathrm{MO}}$), electron
densities ($N_{\mathrm{Rho}}$), transition densities and attach/detach
densities ($N_{\mathrm{DA}}$), to have mesh values calculated.

The final lines specify which MOs, electron densities, transition densities and
CIS attach/detach states are to be plotted (the line can be left blank, or
removed, if the number of items to plot is zero). Molecular orbitals are
numbered $1\ldots N_{\alpha},N_{\alpha}+1\ldots N_{\alpha}+N_{\beta}$; electron
densities numbered where 0= ground state, 1 = first excited state, 2 = second
excited state, *etc.*; and attach/detach specified from state $1\rightarrow N_{\mathrm{DA}}$.

By default, all output data are printed to files in the working directory, overwriting any
existing file of the same name.

- •

Molecular orbital data is printed to a file called `plot.mo`.
- •

Densities are plotted to `plots.hf`.
- •

Restricted unrelaxed attachment/detachment analysis is sent to:

- **–**

`plot.attach.alpha`
- **–**

`plot.detach.alpha`
- •

Unrestricted unrelaxed attachment/detachment analysis is sent to:

- **–**

`plot.attach.alpha`
- **–**

`plot.detach.alpha`
- **–**

`plot.attach.beta`
- **–**

`plot.detach.beta`
- •

Restricted relaxed attachments/detachment analysis is plotted in:

- **–**

`plot.attach.rlx.alpha`
- **–**

`plot.detach.rlx.alpha`
- •

Unrestricted relaxed attachment/detachment analysis is sent to:

- **–**

`plot.attach.rlx.alpha`
- **–**

`plot.attach.rlx.alpha`
- **–**

`plot.attach.rlx.beta`
- **–**

`plot.detach.rlx.beta`

Output is printed in atomic units, with coordinates first followed by item value, as shown below:

> ```qchem
> x1   y1   z1      a1   a2  ...  aN
> x2   y1   z1      b1   b2  ...  bN
> ...
> ```

Instead of a standard one-, two-, or three-dimensional Cartesian grid, a user
may wish to plot orbitals or densities on a set of grid points of his or her
choosing. Such points are specified using a *$grid* input section whose format
is simply the Cartesian coordinates of all user-specified grid points:

> ```qchem
> x1   y1   z1
> x2   y2   z2
> ...
> ```

The *$plots* section must still be specified as described above, but if the
*$grid* input section is present, then these user-specified grid points will
override the ones specified in the *$plots* section.

The **Q-Chem** *$plots* utility allows the user to plot transition densities and
detachment/attachment densities directly from amplitudes saved from a previous
calculation, without having to solve the post-SCF (CIS, RPA, TDA, or TDDFT)
equations again. To take advantage of this feature, the same **Q-Chem** scratch
directory must be used, and the SKIP_CIS_RPA *$rem* variable must be
set to TRUE. To further reduce computational time, the
SCF_GUESS *$rem* can be set to READ.

SKIP_CIS_RPA

### `SKIP_CIS_RPA`

> **Skips the solution of the CIS, RPA, TDA or TDDFT equations for wave function analysis.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE / FALSE
> * **Recommendation**: Set to true to speed up the generation of plot data if the same calculation has been run previously with the scratch files saved.

## 10.5.4.1 New *$plots* input

New format for the *$plots* section provides readable and friendly input for
generation of volumetric data. The input section can be divided into three
parts. The first part contains basic plot options which define the 3-D mesh of
points. The second part contains the selection of densities or orbitals. The
advanced options are included in the last part.

With new plot format, there are multiple ways to define 3-D mesh points. If no
plot option is given, the boundaries of the mesh box are the maximum/minimum
molecular coordinates $\pm~{}3.0$ Å. The default box can be simply enlarged or
reduced by setting `grid_range` to a value larger or smaller than
$3.0$ (negative number is accepted), respectively. To customize the mesh box,
set `grid_range` to desired boundaries:

> ```qchem
> $plots
>   grid_range (-1,1)  (-1,1)  (-1,1)
> $end
> ```

This defines a 2$\times$2$\times$2 mesh box centered at the molecular
coordinate origin. Note that there is no space in the parentheses.

The number of one dimension points is the value of the box length divided by
`grid_spacing`. The default grid point spacing is $0.3$ Å. To override
the usage of `grid_spacing` and customize the number of 3-D points, set
`grid_points` to desired values.

To generate cube file (Section [10.5.5](sec_cubefiles.md)) using new plot format, just
set MAKE_CUBE_FILES = TRUE in *$rem* section. The new plot
format is enabled by requesting PLOTS = 1.

Table 10.3: Options for new *$plots* input section

<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_tt"><span class="ltx_text ltx_font_bold">Option</span></th>
<td class="ltx_td ltx_align_left ltx_border_tt">Explanation</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t"><span class="ltx_text ltx_font_bold">Basic plot options</span></th>
<td class="ltx_td ltx_border_t"></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">grid_range</th>
<td class="ltx_td ltx_wrap ltx_align_left">boundaries${}^{\dagger}$ of the mesh box or increment/decrement in the default boundaries${}^{\dagger\dagger}$ in Å</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">grid_spacing</th>
<td class="ltx_td ltx_align_left">grid point spacing${}^{\dagger\dagger\dagger}$ in Å</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">grid_points</th>
<td class="ltx_td ltx_align_left">
$N_{x}$ $N_{y}$ $N_{z}$
</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t"><span class="ltx_text ltx_font_bold">Density/orbital selection${}^{\star}$</span></th>
<td class="ltx_td ltx_border_t"></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">alpha_molecular_orbital</th>
<td class="ltx_td ltx_align_left">an integer range of alpha MO’s to evaluate</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">beta_molecular_orbital</th>
<td class="ltx_td ltx_align_left">an integer range of beta MO’s to evaluate</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">total_density</th>
<td class="ltx_td ltx_align_left">an integer range of total densities to evaluate</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">spin_density</th>
<td class="ltx_td ltx_align_left">an integer range of spin densities to evaluate</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">transition_density</th>
<td class="ltx_td ltx_align_left">an integer range of transition densities to evaluate</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">natural_transition_orbital</th>
<td class="ltx_td ltx_align_left">an integer range of excited states whose NTOs are evaluated</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">attachment_detachment_density</th>
<td class="ltx_td ltx_align_left">an integer range of det.-att. densities to evaluate</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">natural_bond_orbital</th>
<td class="ltx_td ltx_align_left">an integer range of NBOs for each state to evaluate</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">nbo_state</th>
<td class="ltx_td ltx_align_left">an integer range of states whose NBOs are evaluated</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t"><span class="ltx_text ltx_font_bold">Advanced options</span></th>
<td class="ltx_td ltx_border_t"></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">reduced_density_gradient</th>
<td class="ltx_td ltx_align_left">invoke non-covalent interaction (NCI) plot</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">orbital_laplacians</th>
<td class="ltx_td ltx_align_left">evaluate orbital Laplacians</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">average_local_ionization</th>
<td class="ltx_td ltx_wrap ltx_align_left">evaluate average local ionization energies[[1261]](../bib_references/bib.md#bib1314)
 with a given contour value of the electron density. The default is $0.0135e/\textrm{\AA}^{3}$ ($\approx 0.002e/a^{3}_{0}$).</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">elf</th>
<td class="ltx_td ltx_align_left">invoke electron localization function (ELF) plots</td>
</tr>
</tbody>
<tfoot class="ltx_tfoot">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_tt" colspan="2">
${}^{\dagger}$the format: $(x_{\mathrm{min}},x_{\mathrm{max}})(y_{\mathrm{min}},y_{\mathrm{max}})(z_{\mathrm{min}},z_{\mathrm{max}})$
</th>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row" colspan="2">
${}^{\dagger\dagger}$the default is $3.0$ Å increment in the boundaries derived from the molecular coordinates</th>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row" colspan="2">
${}^{\dagger\dagger\dagger}$the default is $0.3$ Å; it can be overridden by option ’grid_points’</th>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row" colspan="2">
${}^{\star}$input format: n-m or n, indicating n-th oribtal or state; use $0$ for the ground-state</th>
</tr>
</tfoot>
</table>

???+ example "Example 10.25: Generating the cube files: the total densities of the ground and the first
two excited states, the transition and detachment/attachment densities of the
first two excited states, and the 28th to 31th alpha molecular orbitals, with
customized 3-D mesh box and points."
    ```qchem
    $molecule
    0 1
      C    0.0000000   -0.0000000   -0.6133791
      O   -0.0000000    0.0000000    0.6060734
      H    0.0000000    0.9391300   -1.1555819
      H    0.0000000   -0.9391300   -1.1555819
    $end
    
    $rem
       METHOD           cis
       BASIS            6-31+G*
       CIS_N_ROOTS      4
       CIS_TRIPLETS     false
       MAKE_CUBE_FILES  true   ! triggers writing of cube files
       PLOTS            true
    $end
    
    $plots
       grid_range                     (-8,8) (-8,8) (-8,8)
       grid_points                    40 40 40
       total_density                  0-2
       transition_density             1-2
       attachment_detachment_density  1-2
       alpha_molecular_orbital        28-31
    $end
    ```

???+ example "Example 10.26: Generating the cube files of the average local ionization energies and the
total density for the ground state of aniline."
    ```qchem
    $molecule
    0 1
      H        -2.952725   -0.026758    0.000000
      C        -1.871492   -0.010683    0.000000
      C        -1.172124   -0.001127   -1.197270
      H        -1.709244   -0.009471   -2.137819
      C         0.211522    0.017487   -1.202676
      H         0.754733    0.024328   -2.137945
      C         0.916518    0.025234    0.000000
      N         2.357874    0.119819    0.000000
      H         2.747183   -0.346427   -0.829920
      H         2.747183   -0.346427    0.829920
      C         0.211522    0.017487    1.202676
      H         0.754733    0.024328    2.137945
      C        -1.172124   -0.001127    1.197270
      H        -1.709244   -0.009471    2.137819
    $end
    
    $rem
       EXCHANGE         hf
       BASIS            6-31g*
       MAKE_CUBE_FILES  true
       PLOTS            true
    $end
    
    $plots
       grid_spacing   0.1
       total_density  0
       average_local_ionization
    $end
    ```
