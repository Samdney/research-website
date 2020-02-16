title:      		Primes (part 01): Recursion basics
id:                 notes_0001
date:       		2019/05/04 20:00
category:		    Public
categories:		    Public
tags:       		Publication, Notes
author:     		Carolin Zöbelein
slug_dir:           Public
slug_subdir:        Publications
slug:       		Primes-part-01-Recursion-basics
index_title:		Primes (part 01): Recursion basics
index_image:        /images/Notes.jpg
index_summary:		This notes give an overview over all necessary items for calculating prime numbers recursively.
sum_image:			/images/Notes.jpg
sum_content:		This notes give an overview over all necessary items for calculating prime numbers recursively.
kind:               Publication
sub_kind:           Notes
publish_date:       2019/05/04
publication_author: Carolin Zöbelein
subject_class:      2010 Mathematics. Primary 11N05.	
keywords:           Distribution, Primes, Structure, Recursion
pdf:                https://github.com/Samdney/notes/blob/master/notes_0001.pdf
download:           https://github.com/Samdney/notes/raw/master/notes_0001.pdf
links:              GitHub, https://github.com/Samdney/notes-primes01-recursionbasics
links_info:         Source
abstract:           This notes give an overview over all necessary items for calculating prime numbers (only odds, we always ignore number 2) recursively. We start, with the assumption that we know that 3 and 5 are prime numbers. We define equations which gave us all numbers which not belong to their time tables, do an intersection of this, and hence determine the next prime numbers from this. So we can do the same thing again. Taking all our knowing prime numbers, 3, 5 and the new ones, can define equations for the numbers which not belong to this time tables, do an intersection of this, and hence get the new prime numbers. This notes talks about all aspects which we have to consider to do so, and shows that we always have all necessary information to do this recursion without limitations. Since, we are also able to determine a closed analytical equation for the intersection of an arbitrary number of intersection, we are also able to do an recursive considering of it. In future work, it is still necessary to think about a nicer describing equation of this intersection, to find a better presentation of the final recursion formula.


* I. Page 1 - 4: Basic equations and solution of the non-times-table equations intersection
* II. Page 5 - 5: Relationship between old and new (modified) equation
* III. Page 6 - 7: Relationship between old and new (modified) equation - Floor corrections
* IV. Page 8 - 14: General form of the intersection of an arbitrary number of non-times-table
equations
* V. Page 15 - 16: Non-times-table equation correction of Y i to the valid range, by substi-
tution
* VI. Page 17 - 20: Restriction on only odd solutions and the final, general intersection
equation
* VII. Page 21 - 22: Verification that our new (modified) equation is also valid (can used
without restrictions) during every recursion step
* VIII. Page 23 - 27: Determine valid Y i and z i, j ranges
* IX. Page 28 - 28: Approximations for Floor function
* X. Page 29 - 30: Let’s put all together. ToDo.
