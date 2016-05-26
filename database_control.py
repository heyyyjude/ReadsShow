__author__ = 'jwkim'
'''
any comments?
'''

# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.sql import exists
from sqlalchemy.orm import sessionmaker
from cldb import Comm
from collections import namedtuple

from database_info import cldb_url

engine = create_engine(cldb_url,
                       convert_unicode=True)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

roche = namedtuple('roche',
                   (
                       'SampleName', 'Order', 'InitialReads', 'LowQualityReads', 'ShortReads',
                       'DroppedReads', 'Non16sReads', 'ChimeraReads', 'FinalReads',
                   )
                   )

miseq = namedtuple('miseq',
                   (
                       'SampleName', 'Order', 'InitialRawReads', 'MergedReads', 'PrimerTrimmed',
                       'InitialReads', 'LowQualityReads', 'ShortReads', 'DroppedReads', 'Non16sReads', 'ChimeraReads',
                       'FinalReads',
                   )

                   )


def validate_run_id(run_id):
    result = session.query(exists().where(Comm.run_uid == run_id)).scalar()
    return result


def find_454_or_miseq(run_id):
    query = session.query(Comm.machine_id).filter(Comm.run_uid == run_id)
    machine_id = query.first()
    return machine_id


def get_454_sample_reads(run_id):
    query = session.query(Comm.user_sample_name, Comm.order_uid, Comm.n_reads_sort,
                          Comm.n_reads_low_qual, Comm.n_reads_short, Comm.n_reads_drop_primer,
                          Comm.n_reads_hmm_drop, Comm.n_chimera, Comm.n_reads
                          ).filter(Comm.run_uid == run_id).order_by(Comm.sample_uid)

    query_result = query.all()
    sample_result = list()

    for x in query_result:
        sample_result.append(roche(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]))

    sum_result = get_454_sum_reads(sample_result)
    session.close()
    return sample_result, sum_result


def get_454_sum_reads(sample_result):
    sum_result = list()
    sum_total = namedtuple('sum_total',
                           (
                               'InitialReads', 'LowQualityReads', 'ShortReads', 'DroppedReads', 'Non16sReads',
                               'ChimeraReads', 'FinalReads'
                           )
                           )
    inital_total = 0
    lowqual_total = 0
    shortread_total = 0
    droppedread_total = 0
    non16_total = 0
    chimera_total = 0
    final_total = 0

    for x in sample_result:
        inital_total += int(x.InitialReads)
        lowqual_total += int(x.LowQualityReads)
        shortread_total += int(x.ShortReads)
        droppedread_total += int(x.DroppedReads)
        non16_total += int(x.Non16sReads)
        chimera_total += int(x.ChimeraReads)
        final_total += int(x.FinalReads)

    sum_result.append(
        sum_total(
            format(inital_total, ',d'),
            format(lowqual_total, ',d'),
            format(shortread_total, ',d'),
            format(droppedread_total, ',d'),
            format(non16_total, ',d'),
            format(chimera_total, ',d'),
            format(final_total, ',d')
        )
    )
    return sum_result


def get_miseq_sample_reads(run_id):
    query = session.query(Comm.user_sample_name, Comm.order_uid,
                          Comm.n_reads_sort, Comm.n_reads_low_qual, Comm.n_reads_short,
                          Comm.n_reads_drop_primer, Comm.n_reads_hmm_drop, Comm.n_chimera, Comm.n_reads,
                          Comm.comment_internal
                          ).filter(Comm.run_uid == run_id).order_by(Comm.sample_uid)

    query_result = list()
    sample_result = list()

    for x in query:
        tmp_list = list(x)
        tmp_comment = tmp_list[-1]
        tmp_list.remove(tmp_comment)
        for i in tmp_comment.split("|"):
            tmp_list.append(int(i.split(":")[1]))
        query_result.append(tmp_list)

    for x in query_result:
        sample_result.append(miseq
                             (x[0], x[1], x[9], x[10], x[11], x[2], x[3], x[4], x[5], x[6], x[7], x[8])
                             )
    sum_result = get_miseq_sum_reads(sample_result)
    return sample_result, sum_result


def get_miseq_sum_reads(reads_scala):
    sum_total = namedtuple('sum_total',
                           (
                               'InitialRawReads', 'MergedReads', 'PrimerTrimmed', 'InitialReads', 'LowQualityReads',
                               'ShortReads', 'DroppedReads', 'Non16sReads', 'ChimeraReads', 'FinalReads',
                           )
                           )
    init_total = 0
    init_raw_total = 0
    pe_total = 0
    primer_trimmed_total = 0
    low_qual_total = 0
    short_total = 0
    dropped_total = 0
    non_total = 0
    chimera_total = 0
    final_total = 0

    for out_i in reads_scala:
        init_raw_total += out_i.InitialRawReads
        pe_total += out_i.MergedReads
        primer_trimmed_total += out_i.PrimerTrimmed
        init_total += out_i.InitialReads
        low_qual_total += out_i.LowQualityReads
        short_total += out_i.ShortReads
        dropped_total += out_i.DroppedReads
        non_total += out_i.Non16sReads
        chimera_total += out_i.ChimeraReads
        final_total += out_i.FinalReads

    sum_result = list()
    sum_result.append(
        sum_total(
            format(init_raw_total, ',d'),
            format(pe_total, ',d'),
            format(primer_trimmed_total, ',d'),
            format(init_total, ',d'),
            format(low_qual_total, ',d'),
            format(short_total, ',d'),
            format(dropped_total, ',d'),
            format(non_total, ',d'),
            format(chimera_total, ',d'),
            format(final_total, ',d')
        )
    )
    return sum_result
