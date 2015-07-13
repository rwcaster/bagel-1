## Reviewer: 1 ## Recommendation: Publish after major revisions noted. 

> This is an interesting and ambitious manuscript in which a substantial
> library of mutants of a structurally characterised GH1 glycosidase has
> been made, the mutant enzymes purified and kinetic parameters determined
> for a single substrate (p-nitrophenyl -D-glucopyranoside).  The work
> seems to be, for the most part, well done and the results of value. I am
> not convinced we learn a lot yet that is of value from the application of
> machine learning approaches here…but I fully agree we need better
> databases to make a start in this direction. 

... 

> The analysis could do with a little deeper thinking in places. For
> example, the authors are trying to interpret kinetic parameters, but they
> never discuss what step is rate-limiting for the wild type enzyme, let
> alone for the mutants, with the particular substrate they have employed.
> This is rather important information as the rate-determining step may
> change between mutants. Indeed I am pretty sure this is the case for
> several mutants. My guess, from the data (mostly from the Km values) is
> that the formation of the glycosyl-enzyme intermediate is
> rate-determining for most. However for some such as E164A and E222A
> I would bet that hydrolysis of this intermediate has become
> rate-limiting, thus the second step has been slowed more than the first
> by the mutations for some reason. This is easy to understand for E164
> when using a “good” substrate, but why E222? 

We fully agree that our modeling, which uses a possible representative of
the transition state, does not fully capture all possible transition states
in the hydrolysis of pNPG, and that, for certain mutants, the transition
state is likely different from the TSS in the wild type enzyme. In future,
we may want to include such multi-state modeling. 

> Likewise analysis is very light with regard to relating these data to the
> extensive literature on kinetic analysis of other GH1 glycosidases as
> well as other members of Clan GHA, which all have the same fold and
> largely the same set of active site residues…and lots of careful analysis
> of substantial numbers of mutants in many cases with multiple substrates.
> Likewise careful measurements have been made of kinetic parameters for
> hydrolysis of selectively “mutated” substrates (deoxy etc) for GH1 and
> other Clan GHA glycosidases …with much attention paid to issues of
> changes in rate-determining steps. These data are all highly relevant to
> what is being discussed here…so should be part of a broader analysis. 

> The work should also reference the very recent PNAS paper
> ( www.pnas.org/cgi/doi/10.1073/pnas.1422285112) on functional analysis of
> huge libraries of mutants of a GH1 glycosidase using microfluidic
> methodologies and deep sequencing. 

We are grateful to reviewer 1 for the link to this article, and will revise
the manuscript to make reference to it as part of a deeper analysis. 

# Reviewer: 2 

*Recommendation*: Not suitable for publication at this time. 

Comments: New, more effective strategies for protein re-design are highly
sought after by the biocatalysis community. In this manuscript, Carlin et
al. present a new semi-rational approach combining the Rosetta Design
algorithm, systematic experimental evaluation of enzyme variants and
machine-learning to identify key residues in beta-glucosidase B,
a glycoside hydrolase from Paenibacillus polymyxa. The computational models
identify 69 amino acid positions, 44 of them within 12 angstrom of the
active site which were examined by alanine-scanning mutagenesis. The
remaining positions were identified for their capacity to allow amino acid
substitutions without impacting the transition-state model. Based on these
positions, a gene library of 104 glycosides mutants was synthesized, the
corresponding proteins expressed in E. coli and purified. Finally, the
kinetic properties determined by steady-state kinetics. The functional data
was used in correlation analyses f! or the kinetic parameters. 

> Overall, this is an interesting but very preliminary set of results. All
> major conclusions are based on multiple layers of modeling, adding
> variability and uncertainty to the findings. Moreover, the conclusions from
> the present data are very limited and only confirm obvious effects (see
> example of Q19A mentioned below). Beyond the 44 positions near the active
> site, the manuscript mentions and lists an additional 25 amino acid
> substitutions (based on FoldIt analysis), yet these variants are not
> further discussed. Finally, the work is incomplete as it never demonstrates
> that information from the machine-learning algorithm can effectively been
> utilized to actually improve the enzyme. 

We thank reviewer 2 for comments regarding the scope of the manuscript.
However, we would like to point out that the recapitulatization of
so-called "obvious" functional effects of mutations is actually vindication
of our strategy's physically-realistic scoring. Furthermore, the goal of
this paper is not to deeply describe the functional effects of a small
number of obvious mutations, but rather to use machine learning to identify
computational metrics that correlate with observed functional effects of
mutations in order to pave the way for a predictive algorithm that can
predict kcat and Km for variants of BglB. Yet further, we are deeply
uninterested in "improving" BglB by this method. Methods for designing
enzymes with specific kinetic parameters are beyond the scope of this work. 


> There are additional concerns: 

> - Throughout the manuscript, the authors occasionally refer to the
>  different glucosidase enzymes as mutants, rather than variants. Please
>  correct. 

Respectfully, both are correct. 

> - On page 4, the authors claim to have measured kcat, Km, and Ki values for
>  their library members. However, Ki values are only reported for 11 of the
>  candidates. Please correctly state the included data. 

Will do!

> - Figure 2; the color choices for the heat map are hard to distinguish.
>  A wider selection of the color spectrum would help readers to more easily
>  differentiate the seven distinct performance levels. 

We agree that the heatmap color scheme leaves something to be desired.
Perhaps a solution to this would be to replace the current gradient color
scheme with another where "neutral" mutations are marked as gray, and for
each of "lower" and "higher", three orders of magnitude are reported with
distinct colors. 

> - The citations of relevant previous work is somewhat Rosetta-centric.
>  While the present work is based on this design algorithm, the manuscript
>  would benefit from additional references to more broadly represent the
>  protein engineering literature using machine-learning as a strategy for
>  functional improvements.  Examples include but should not be limited to:
>  Minshull et al. (2005) Curr Opin Chem Biol. 9:202; Liao et al. (2007) BMC
>  Biotech 7:16; Govindarajan et al. (2014) ACS Synth Biol. 4:221. 

We are happy to cite these papers if they add something to our discussion. 

> - Page 8; the significant functional impact of Q19A is overhyped. As shown
>  in Fig. 3A, the residue is a key binding partner in the active site as
>  also reflected in its >95% conservation. The authors’ surprise that an
>  amino acid change to alanine causes a dramatic change in catalytic
>  performance seems hard to believe. Substrate binding and pre-orientation
>  are critical to effective catalysis, so the functional change is nothing
>  be to be expected. 

We can change the wording here so it is clear that this mutation's
functional effects are in line with previous work on this enzyme. 

# Reviewer: 3 
# Recommendation: Not suitable for publication at this time. 

Comments: The manuscript cs-2015-01106z reports the effort to correlate
kinetic parameters of ~90 mutants that have been generated by Rosetta
Molecular Modeling Suite. These mutants were overexpressed and their Km and
kcat measured. 

> However, a major deficiency of the report is the lack of a conclusive
> learning outcome. This is because there is no clear principle for
> correlating kinetic parameters such as Km, kcat or kcat/Km with force-field
> based algorithms. Before making use of these kinetic parameters, one should
> be able to explain what kinetic model is associated with this enzyme. How
> many catalytic steps and kinetic constants are involved? How would the
> change of each residue affect each kinetic constant? What is the definition
> of Km in this enzyme? Km is not always equal to Kd (dissociation constant,
> binding affinity). Km is correlated with Kd only if binding steps are fast
> and a step afterward (such as hydrolysis) is much slower. In my opinion, it
> would be impossible to correlate Km with any force-field based algorithms.
> In the paper, the authors correlated 1/Km, which is even more confusing.
> Perhaps, it may be possible to correlate kcat with force-field algorithms
> if the rate-limiting step of the reaction is known, and it is well
> understood how the change of active site affects the transition state of
> the rate-limiting step. However, I anticipate that not all mutants within
> this large set of mutants will have the same rate-limiting step. 

Wow. Just wow. 

