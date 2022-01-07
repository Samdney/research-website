#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date
from datetime import time
from datetime import datetime


# TODO: related: Works, Project(s), Funding/Grants, Talks, ...
# TODO: bib entries numberings brackets

# TODO: Add missing entry information
# TODO: Remove old subpages

BIBLIOGRAPHY_LASTUPDATE = '2021/08/28'

BIBLIOGRAPHY = (
    #('nb', 'title', 'sum', 'author', 'date', 'year', 'kind', 'keywords', 'subjectclass', 'subjects', 'publication', 'publicationlink', 'preprint', 'latex', 'source', 'pdf', 'related', 'misc', 'doi', 'id', 'abstract'),

    ('7', 'HG-hybrid graphs', '', 'Carolin Zöbelein', '', '2021', 'Draft', '', '', 'Math, CS', '', '', '', '', '', '', '', '', '', '', 
        ''),

    ('6', 'Powers of 2 whose digits are powers of 2', '', 'Carolin Zöbelein', '', '2021', 'Preprint', '', '', 'Math', '', '', '', '', '', '', '', '', '', 'paper_0004', 
        ''),

    ('5', 'Dynamical decomposition by clique separators on hypergraphs', '', 'Carolin Zöbelein', '', '2021', 'Preprint', '', '', 'Math, CS', '', '', '', '', '', '', '', '', '', 'paper_0003', 
        ''),

    ('4', 'Primitive data structures for the 3SUM and k-SUM problem', '', 'Carolin Zöbelein', '', '2021', 'Preprint', '', '', 'Math, CS', '', '', '', '', '', '', '', '', '', 'paper_0002',
        'We discuss the usage of primitive data structures for the 3SUM, respectively kSUM problem for integers and real numbers. We show, that we can map the case of rational numbers on the integer case by introducing a new data structure fixedint for an universe U := 2^{2N −1} , with integers represented by N bits each. Furthermore, we show that we can map the case of irrational numbers on the integer case, too. For this, we introduce a new data structure realnumber and get a belonging universe U_{qV ec} := 2^{(2N −1)(1+|I_{a}|)} with a maximum possible value |2^{2N −1} (1 + |I_{a}| max(I_{a}))|.'),

    ('3', 'BlueTransience', 'A Bluetooth based, short memory, social media mobile network app', 'Carolin Zöbelein', 'March 26, 2021', '2020', 'Proposal', ' Bluetooth, Mobile App, Social Media, Natural Disaster, Political Demonstrations, Internet Shutdown', '', 'CS', ' Authorea', 'https://www.authorea.com/users/402885/articles/515244-proposal-bluetransience', '', 'https://github.com/Samdney/proposal-bluetransience', '', '', '', '', 'https://doi.org/10.22541/au.161676845.56300213/v1', 'proposal_0001', 
        'A Bluetooth based, short memory, social media mobile network app.'),

    ('2', 'About the proof of the Collatz conjecture', 'I want to show one possibility to proof the Collatz conjecture, also called 3n+1 conjecture, for any natural number N.', 'Carolin Zöbelein', '', '2013', 'Preprint', '', '2010 Mathematics. Primary 11N05', 'Math', '', '', 'https://arxiv.org/abs/1303.2073', 'https://github.com/Samdney/paper-collatz', '', 'paper_0001.pdf', '', '', '', 'paper_0001', 
        'I want to show one possibility to proof the Collatz conjecture, also called 3n + 1 conjecture, for any natural number N ∈ N. For this, I limit my analysis on the direct odd follower of every natural odd number and show the connections between the already by one reached numbers and their followers, to find an recurrence over all ranges [1, N_{i}], i ∈ N to proof the conjecture.'),

    ('1', 'Dirac Observablen in der Kosmologie', '', 'Carolin Zöbelein', '', '2013', 'Bachelor Thesis', '', '2010 PACS. 4.60.-m, 98.80.-k', 'Physics', '', '', '', '', '', '', '', '', '', 'thesis_0001', 
        '')
)

