EDI Message Parsing
###################

:date: 2023-03-17 08:00
:tags: architecture,software design,data structure,algorithm,edi,x12
:slug: 2023_03_17-edi_message_parsing
:category: Technologies
:status: published

Reaching back to 2008. Yes. Decade(s) ago. Python 2.5.

I was reminded of this when a former colleague
pinged me about this: https://github.com/slott56/TigerShark.

Yes, it's an X12/EDI message parsing library from -- well -- decades ago.

What is all this about?
=======================

Short answer: Parsing X12 EDI messages, which have an obscure-as-hell structure.

Long Answer: EDI (Electronic Data Interchange) is a way
for business enterprises and government agencies to exchange
data in well-defined formats. See https://www.edibasics.com/what-is-edi/.

It sounds so simple and generic. It's so old, it predates
HTML, XML, JSON, etc. Therefore, the formats are -- well -- weird.

There's a "standard", X12, that defines these messages.
See https://x12.org. See https://www.stedi.com/edi/x12.

But. The exchange of message used to be done through proprietary networks
and software. Therefore the compliance with the standard
is sometimes incomplete. (Remember, this is **old**.)

Back In The Day
===============

Some history

- `Python as Config Language -- Forget XML and INI files <{filename}/blog/2008/01/2008_01_12-python_as_config_language_forget_xml_and_ini_files.rst>`_

- `Two Python Config-File Design Patterns <{filename}/blog/2008/01/2008_01_19-two_python_config_file_design_patterns.rst>`_

- `Configuration File Scalability -- Who Knew? (Revised) <{filename}/blog/2008/01/2008_01_26-configuration_file_scalability_who_knew_revised.rst>`_

- `Technical Debt, the Cost of Cheap and "Get This Done ACAP" <{filename}/blog/2008/03/2008_03_08-technical_debt_the_cost_of_cheap_and_get_this_done_acap.rst>`_

- `Synchronicity and Document Object Models <{filename}/blog/2008/03/2008_03_31-synchronicity_and_document_object_models.rst>`_

- `POPO and GOPS - Plain Old Python Objects and Good Old Python Syntax <{filename}/blog/2008/04/2008_04_01-popo_and_gops_plain_old_python_objects_and_good_old_python_syntax.rst>`_

I wrote an X12 parser in Python.

It transforms X12 text into Plain Old Python Objects (POPO.)

Back in the day (2008) this was targeted for Python 2.5.

It's Time
=========

Nowadays, this is does **not** need to be quite so complicated.

Modern Python has a few changes since release 2.5.
Two are central to this project:

- type annotations

- classes maintain the order of the definitions

These are the backbone of `dataclasses <https://docs.python.org/3/library/dataclasses.html>`_ (and `pydantic <https://docs.pydantic.dev>`_ and `attrs <https://www.attrs.org/en/stable/>`_.)

I believe there are two parts to the rewrite.

1. Create dataclass-like class definition for segments and loops. These generally come from the non-Python configuration files used elsewhere. The Python is built from this. Once.

2. Create a generic parser protocol that can extract the segments, loops, and atomic fields from the X12 messages. This becomes a superclass feature of all X12 components.

This should be much simpler than the old version. Which was **very** complicated.
The old release had two levels of interpretation of the X12 content:

- Generic segments and loops

- A Pythonic **Façade** over the generic structure

I think this was (and continues to be) a bad idea.

(Progress will be flaky. I have a book to write, also.)

First Things First
==================

Some updates to reflect Python 3.11 and better GitHub practices.
I'll make the documentation more visible as a first step.
I may rewrite the diagrams to PlantUML, also.

Just a few small cleanups before throwing the entire
thing away and beginning again.
