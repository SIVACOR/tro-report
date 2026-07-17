# {TRACE logo} Transparency Certified (TRACE) certificate for SIVACOR {SIVACOR logo}

<!-- Generic header -->
**This document certifies execution by the {{ trov:name }} system in line with the TRACE specification. It accompanies the trusted research object (TRO) identified by {{ expand id:fingerprint }}.**

In particular, every TRACE-compatible system executes code on user-prepared packages of code and data, without further interaction with the user. 

<!-- System specific header -->

The {{ trov:name }} is controlled by {{ trov:owner }}. Additional information can be found at <{{ trov:url }}>.

This specific system has several capabilities, listed in the Appendix. The specific capabilities exercised during the execution may vary from step to step, and are identified in the technical records.

<!-- System specific disclaimer - read from TRO -->

(DISCLAIMER) This certificate only describes the execution of the code by {{ trov:name }}. It does not certify the correctness of the analysis conducted therein, nor consistency with any statements in manuscripts or documents that refer to this TRO.


To find out more about TRACE, see the [TRACE project page](https://transparency-certified.github.io/).

## Overview

This report lists one more transparent research performance (TRP) which transformed arrangements of files into subsequent arrangements of files. The report identifies files that were created, modified, and removed throughout the process.



## Details on TRPs and arrangements

- SIVACOR observed **two** arrangements:
   - Arrangement 0: `Before executing workflow` 
   - Arrangement 1: `After executing workflow step 1`
- SIVACOR executed **one** transparent research performance (TRP):
   - TRP 0: `SIVACOR workflow execution (run_everything.do) step 1`

{{ flow diagram specific to the observed TRO }}

[ Arrangement 0 ]  -->  [ TRP 0         ]  -->  [Arrangement 1] 
                        [ Software name ]

## Changes in arrangements

- Initial arrangement: 95 paths. Final arrangement: 96 paths.
- SIVACOR recorded 1 new path, 0 removed paths, and 9 modified paths between the initial and final arrangements.
- Generated new output paths included 0 paths: 0 table paths, 0 figure paths.
- The full SIVACOR arrangement comparison is listed in the Appendix.
- SIVACOR is used here to document execution and generated files. It is not designed to compare figures and tables against the manuscript.
The SIVACOR TRO records the following execution environment(s):

TRP 0: 

- SIVACOR Job ID: `6a316ed464efec49e59c464b`
- Processor: AMD EPYC-Milan Processor
- CPUs: 16
- Total memory: 58.8 GB
- Operating system: Ubuntu 24.04.4 LTS (Version 24.04)
- Kernel version: 6.17.0-23-generic
- Container image(s): `dataeditors/stata19_5-mp-i-python:2026-04-15` (`dataeditors/stata19_5-mp-i-python@sha256:7921f4ee992eecc51cf254365f057666645e3df9e581d021bf815119ef3cb36e`)

### SIVACOR arrangement comparison

SIVACOR arrangement comparison from `Before executing workflow` to `After executing workflow step 1`.

- Initial arrangement: 95 paths.
- Final arrangement: 96 paths.
- New paths: 1.
- Removed paths: 0.
- Modified paths: 9.

#### Generated table output paths

Tables are identified as XLSX, TEX, or TXT files. This may capture data output as well.

- None recorded.

#### Generated figure output paths

Figures are identified from typical graph output extensions, generic (PNG, SVG, EPS, PDF, etc.) and software-specific (Stata GPH, MATLAB FIG files, etc.)

- None recorded.

#### Generated log paths

Files ending in `*.log`, `.*out` or similar are recorded here.

- `run_everything.log`

#### Other generated output paths

Any files not listed above and observed as new files relative to the initial arrangement are listed here.

- None recorded.

#### Removed paths

Any files removed are listed here. When there are more than two arrangements, the step in which they were removed is listed. Files created and removed within a single step are not identifiable. Files created in one step, removed in a later step are marked with additional information. 

- None recorded.

#### Modified paths

Any files present originally, but modified at some point, are listed here. When there are more than two arrangements, the steps in which they were modified are listed. 

- `data/feasible.csv`
- `output/figures/Individual_agency_ratings_2s2023.pdf`
- `output/figures/Worker_skill_and_outcomes2023.pdf`
- `output/figures/employment_and_others_skill.pdf`
- `output/figures/hiding_news2026.pdf`
- `output/figures/iso-profit-curves_percent_with_predictions2023.pdf`
- `output/tables/reg_employed_avgothersskill_round2023.tex`
- `output/tables/reg_employed_skill.tex`
- `output/tables/reg_stars_lags.tex`
