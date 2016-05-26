__author__ = 'jwkim'
'''
any comments?
'''

# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Enum, Float, Index, Integer, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import MEDIUMBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Assembler(Base):
    __tablename__ = 'assembler'

    uid = Column(Integer, primary_key=True)
    name = Column(String(250))
    comment = Column(Text)


class Barcode(Base):
    __tablename__ = 'barcode'

    uid = Column(Integer, primary_key=True)
    user_group_uid = Column(Integer, server_default=text("'1'"))
    sequence = Column(String(8), nullable=False)
    primer = Column(String(250))


class ChunlabJob(Base):
    __tablename__ = 'chunlab_job'

    uid = Column(Integer, primary_key=True)
    stamp_update = Column(DateTime, nullable=False, server_default=text("'2000-01-01 03:00:00'"))
    stamp_insert = Column(DateTime, nullable=False, server_default=text("'2000-01-01 03:00:00'"))
    comment_internal = Column(String)
    owner_uid = Column(Integer, nullable=False)
    reaction_by = Column(String(20))
    reaction_date = Column(String(10))


class ClNew(Base):
    __tablename__ = 'cl_news'

    uid = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    article = Column(String, nullable=False)
    time_write = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class Cog(Base):
    __tablename__ = 'cog'

    id = Column(String(30), primary_key=True)
    category = Column(String(30), nullable=False)
    function = Column(String(250), nullable=False)


class CogOrganism(Base):
    __tablename__ = 'cog_organism'

    id = Column(String(3), primary_key=True)
    tax_id = Column(Integer, server_default=text("'-1'"))
    tax_group = Column(String(100), nullable=False)
    name = Column(String(250), nullable=False)


class CogProtein(Base):
    __tablename__ = 'cog_protein'

    id = Column(String(30), primary_key=True)
    cog_id = Column(String(30))
    category = Column(String(30))
    gi = Column(Integer, server_default=text("'-1'"))
    organism = Column(String(3))
    sequence = Column(Text, nullable=False)


class Comm(Base):
    __tablename__ = 'comm'

    uid = Column(Integer, primary_key=True)
    stamp_update = Column(DateTime, nullable=False, server_default=text("'2000-01-01 00:00:00'"))
    stamp_insert = Column(DateTime, nullable=False, server_default=text("'2000-01-01 00:00:00'"))
    comment_user = Column(String)
    comment_internal = Column(String)
    user_group_uid = Column(Integer, index=True, server_default=text("'-1'"))
    user_uid = Column(Integer, index=True, server_default=text("'-1'"))
    order_uid = Column(Integer, index=True, server_default=text("'-1'"))
    sample_uid = Column(Integer, index=True, server_default=text("'-1'"))
    user_sample_name = Column(String(250))
    user_sample_name_modified = Column(String(250))
    sampling_date = Column(Date)
    source_keywords = Column(String(250))
    sample_description = Column(Text)
    run_uid = Column(Integer, index=True, server_default=text("'-1'"))
    machine_id = Column(Integer, server_default=text("'-1'"))
    gene = Column(String(250), index=True, server_default=text("'N/A'"))
    target_taxon = Column(String(250), server_default=text("'N/A'"))
    primer_for = Column(String(100))
    primer_rev = Column(String(100))
    barcode = Column(String(100))
    linker_for = Column(String(100))
    linker_rev = Column(String(100))
    n_reads = Column(Integer, server_default=text("'-1'"))
    min_len = Column(Integer, server_default=text("'-1'"))
    max_len = Column(Integer, server_default=text("'-1'"))
    average_len = Column(Float(asdecimal=True), server_default=text("'-1'"))
    n_phylotypes = Column(Integer, server_default=text("'-1'"))
    country = Column(String(250))
    coord_NS = Column(String(100))
    coord_EW = Column(String(100))
    n_reads_sort = Column(Integer, server_default=text("'-1'"))
    average_len_sort = Column(Float(asdecimal=True), server_default=text("'-1'"))
    n_reads_for = Column(Integer, server_default=text("'-1'"))
    n_reads_rev = Column(Integer, server_default=text("'-1'"))
    n_reads_short = Column(Integer, server_default=text("'-1'"))
    n_reads_low_qual = Column(Integer, server_default=text("'-1'"))
    n_reads_drop_primer = Column(Integer, server_default=text("'-1'"))
    n_reads_both = Column(Integer, server_default=text("'-1'"))
    n_reads_blast_drop = Column(Integer, server_default=text("'-1'"))
    n_reads_hmm_drop = Column(Integer, server_default=text("'-1'"))
    n_chimera = Column(Integer, server_default=text("'-1'"))
    n_contig_0 = Column(Integer, server_default=text("'-1'"))
    comm_struct = Column(String)
    length_stat = Column(String)
    db_gene = Column(String(200))
    db_ver = Column(String(200))
    db_taxon = Column(String(200))
    b_read_sort_done = Column(Integer, server_default=text("'-1'"))
    b_primer_drop_done = Column(Integer, server_default=text("'-1'"))
    b_blast_drop_done = Column(Integer, server_default=text("'-1'"))
    b_hmm_drop_done = Column(Integer, server_default=text("'-1'"))
    b_read_done = Column(Integer, server_default=text("'-1'"))
    b_contig_0_done = Column(Integer, server_default=text("'-1'"))
    b_cm_done = Column(Integer, server_default=text("'-1'"))
    b_community_done = Column(Integer, server_default=text("'-1'"))
    b_contig_0_zip_done = Column(Integer, server_default=text("'-1'"))
    b_sff_done = Column(Integer, server_default=text("'-1'"))
    cdhit_otu = Column(Integer, server_default=text("'-1'"))
    cdhit_stat = Column(Text)
    cdhit_rf = Column(String)
    cdhit_singleton = Column(Integer, server_default=text("'-1'"))
    cdhit_chao = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_chao = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_chao_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_chao_lci_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_chao_hci_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_chao_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_chao_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_chao_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_chao_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_ace = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_ace = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_ace_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_ace_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_ace_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_ace_hci_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_ace_lci_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_ace_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_ace_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_jackknife = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_jackknife = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_jackknife_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_jackknife_lci_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_jackknife_hci_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    share_user_group = Column(String(50))
    share_user_uid = Column(String(500))
    cdhit_jackknife_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_jackknife_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_jackknife_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_jackknife_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_shannon = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_shannon = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_npshannon_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_simpson_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_simpson_lci_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_simpson_hci_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_shannon_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_shannon_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_shannon_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_shannon_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_shannon_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_npshannon = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_shannon_hci_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_shannon_lci_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_npshannon = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_rf_target = Column(String)
    cdhit_simpson = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_simpson = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_simpson_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_simpson_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_simpson_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_simpson_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_otu = Column(Integer, server_default=text("'-1'"))
    blast_rf = Column(String)
    phylum_comp = Column(String(255))
    altitude = Column(Float(asdecimal=True), server_default=text("'0'"))
    reference = Column(String(250))
    gb_acc = Column(String(50))
    coord_NS_type = Column(String(1), server_default=text("'N'"))
    coord_EW_type = Column(String(1), server_default=text("'E'"))
    roche_mid = Column(String(20))
    cdhit_otu_target = Column(Integer)
    cdhit_chao_target = Column(Float(asdecimal=True))
    cdhit_rf_target = Column(String)
    cdhit_singleton_target = Column(Integer)
    cdhit_chao_lci_target = Column(Float(asdecimal=True))
    cdhit_chao_hci_target = Column(Float(asdecimal=True))
    cdhit_ace_target = Column(Float(asdecimal=True))
    cdhit_ace_lci_target = Column(Float(asdecimal=True))
    cdhit_ace_hci_target = Column(Float(asdecimal=True))
    cdhit_jackknife_target = Column(Float(asdecimal=True))
    cdhit_jackknife_lci_target = Column(Float(asdecimal=True))
    cdhit_jackknife_hci_target = Column(Float(asdecimal=True))
    cdhit_npshannon_target = Column(Float(asdecimal=True))
    cdhit_shannon_target = Column(Float(asdecimal=True))
    cdhit_shannon_lci_target = Column(Float(asdecimal=True))
    cdhit_shannon_hci_target = Column(Float(asdecimal=True))
    cdhit_simpson_target = Column(Float(asdecimal=True))
    cdhit_simpson_lci_target = Column(Float(asdecimal=True))
    cdhit_simpson_hci_target = Column(Float(asdecimal=True))
    b_clc_done = Column(Integer, server_default=text("'-1'"))
    n_reads_target = Column(Integer, server_default=text("'-1'"))
    cdhit_good_library = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_otu_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_good_library_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_singleton_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_singleton = Column(Float(asdecimal=True), server_default=text("'-1'"))
    update_type = Column(Enum(u'once', u'year'), server_default=text("'once'"))
    update_count = Column(Integer, server_default=text("'0'"))
    comm_ver = Column(Float(asdecimal=True), server_default=text("'0'"))
    primer_set = Column(Integer)
    db_info = Column(String(100))
    blast_good_library = Column(Float(asdecimal=True))
    blast_good_library_target = Column(Float(asdecimal=True))


class CommProfile(Base):
    __tablename__ = 'comm_profile'

    pfid = Column(String(50), primary_key=True)
    db_uid = Column(String(50), nullable=False)
    created_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    profile = Column(MEDIUMBLOB, nullable=False)


class CommWeb(Base):
    __tablename__ = 'comm_web'

    uid = Column(Integer, primary_key=True)
    stamp_update = Column(DateTime, nullable=False, server_default=text("'2000-01-01 00:00:00'"))
    stamp_insert = Column(DateTime, nullable=False, server_default=text("'2000-01-01 00:00:00'"))
    comment_user = Column(String)
    comment_internal = Column(String)
    user_group_uid = Column(Integer, index=True, server_default=text("'-1'"))
    user_uid = Column(Integer, server_default=text("'-1'"))
    user_sample_name = Column(String(250))
    sampling_date = Column(Date)
    source_keywords = Column(String(250))
    sample_description = Column(Text)
    run_uid = Column(Integer, server_default=text("'-1'"))
    machine_id = Column(Integer, server_default=text("'-1'"))
    gene = Column(String(250), index=True, server_default=text("'N/A'"))
    target_taxon = Column(String(250), server_default=text("'N/A'"))
    primer_for = Column(String(100))
    primer_rev = Column(String(100))
    barcode = Column(String(100))
    linker_for = Column(String(100))
    linker_rev = Column(String(100))
    n_reads = Column(Integer, server_default=text("'-1'"))
    min_len = Column(Integer, server_default=text("'-1'"))
    max_len = Column(Integer, server_default=text("'-1'"))
    average_len = Column(Float(asdecimal=True), server_default=text("'-1'"))
    n_phylotypes = Column(Integer, server_default=text("'-1'"))
    country = Column(String(250))
    coord_NS = Column(String(100))
    coord_EW = Column(String(100))
    n_reads_sort = Column(Integer, server_default=text("'-1'"))
    average_len_sort = Column(Float(asdecimal=True), server_default=text("'-1'"))
    n_reads_for = Column(Integer, server_default=text("'-1'"))
    n_reads_rev = Column(Integer, server_default=text("'-1'"))
    n_reads_drop_primer = Column(Integer, server_default=text("'-1'"))
    n_reads_both = Column(Integer, server_default=text("'-1'"))
    n_reads_blast_drop = Column(Integer, server_default=text("'-1'"))
    n_reads_hmm_drop = Column(Integer, server_default=text("'-1'"))
    n_chimera = Column(Integer, server_default=text("'-1'"))
    n_contig_0 = Column(Integer, server_default=text("'-1'"))
    comm_struct = Column(String)
    length_stat = Column(String)
    db_gene = Column(String(200))
    db_ver = Column(String(200))
    db_taxon = Column(String(200))
    b_read_sort_done = Column(Integer, server_default=text("'-1'"))
    b_primer_drop_done = Column(Integer, server_default=text("'-1'"))
    b_blast_drop_done = Column(Integer, server_default=text("'-1'"))
    b_hmm_drop_done = Column(Integer, server_default=text("'-1'"))
    b_read_done = Column(Integer, server_default=text("'-1'"))
    b_contig_0_done = Column(Integer, server_default=text("'-1'"))
    b_cm_done = Column(Integer, server_default=text("'-1'"))
    b_community_done = Column(Integer, server_default=text("'-1'"))
    b_contig_0_zip_done = Column(Integer, server_default=text("'-1'"))
    b_sff_done = Column(Integer, server_default=text("'-1'"))
    cdhit_otu = Column(Integer, server_default=text("'-1'"))
    cdhit_stat = Column(Text)
    cdhit_rf = Column(String)
    cdhit_singleton = Column(Integer, server_default=text("'-1'"))
    cdhit_chao = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_chao = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_chao_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_chao_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_chao_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_chao_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_ace = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_ace = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_ace_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_ace_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_ace_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_ace_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_jackknife = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_jackknife = Column(Float(asdecimal=True), server_default=text("'-1'"))
    share_user_group = Column(String)
    cdhit_jackknife_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_jackknife_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_jackknife_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_jackknife_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_shannon = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_shannon = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_shannon_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_shannon_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_shannon_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_shannon_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_npshannon = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_npshannon = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_simpson = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_simpson = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_simpson_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_simpson_lci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_simpson_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_simpson_hci = Column(Float(asdecimal=True), server_default=text("'-1'"))
    blast_otu = Column(Integer, server_default=text("'-1'"))
    blast_rf = Column(String)
    phylum_comp = Column(String(255))
    altitude = Column(Float(asdecimal=True), server_default=text("'0'"))
    reference = Column(String(250))
    gb_acc = Column(String(50))
    coord_NS_type = Column(String(1), server_default=text("'N'"))
    coord_EW_type = Column(String(1), server_default=text("'E'"))
    roche_mid = Column(String(20))
    cdhit_otu_target = Column(Integer)
    cdhit_chao_target = Column(Float(asdecimal=True))
    cdhit_rf_target = Column(String)
    cdhit_singleton_target = Column(Integer)
    cdhit_chao_lci_target = Column(Float(asdecimal=True))
    cdhit_chao_hci_target = Column(Float(asdecimal=True))
    cdhit_ace_target = Column(Float(asdecimal=True))
    cdhit_ace_lci_target = Column(Float(asdecimal=True))
    cdhit_ace_hci_target = Column(Float(asdecimal=True))
    cdhit_jackknife_target = Column(Float(asdecimal=True))
    cdhit_jackknife_lci_target = Column(Float(asdecimal=True))
    cdhit_jackknife_hci_target = Column(Float(asdecimal=True))
    cdhit_npshannon_target = Column(Float(asdecimal=True))
    cdhit_shannon_target = Column(Float(asdecimal=True))
    cdhit_shannon_lci_target = Column(Float(asdecimal=True))
    cdhit_shannon_hci_target = Column(Float(asdecimal=True))
    cdhit_simpson_target = Column(Float(asdecimal=True))
    cdhit_simpson_lci_target = Column(Float(asdecimal=True))
    cdhit_simpson_hci_target = Column(Float(asdecimal=True))
    b_clc_done = Column(Integer, server_default=text("'-1'"))
    n_reads_target = Column(Integer, server_default=text("'-1'"))
    cdhit_good_library = Column(Float(asdecimal=True), server_default=text("'-1'"))
    cdhit_good_library_target = Column(Float(asdecimal=True), server_default=text("'-1'"))
    update_type = Column(Enum(u'once', u'year'), server_default=text("'once'"))
    update_count = Column(Integer, server_default=text("'0'"))
    comm_ver = Column(Float(asdecimal=True), server_default=text("'0'"))


class Country(Base):
    __tablename__ = 'country'

    uid = Column(Integer, primary_key=True)
    engname = Column(String(100), nullable=False, server_default=text("''"))


class ExampleRun(Base):
    __tablename__ = 'example_run'

    run_id = Column(Integer, primary_key=True)
    run_name = Column(String(300))
    status = Column(String(10))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP"))


class ExampleSample(Base):
    __tablename__ = 'example_sample'

    sample_id = Column(Integer, primary_key=True)
    run_id = Column(Integer, nullable=False)
    sample_name = Column(String(300))
    sample_description = Column(Text)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP"))


class FileMainInfo(Base):
    __tablename__ = 'file_main_info'

    fileId = Column(Integer, primary_key=True)
    userId = Column(String(50), nullable=False, server_default=text("'0'"))
    fileName = Column(String(200), nullable=False, unique=True)
    fileType = Column(String(50))
    fileLocation = Column(String(200))
    fileSize = Column(BigInteger, server_default=text("'0'"))
    createdTime = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    modifiedTime = Column(DateTime)
    pipelineTime = Column(DateTime)


t_file_meta_info = Table(
    'file_meta_info', metadata,
    Column('fileId', Integer),
    Column('paramName', String(100)),
    Column('paramValue', String(200))
)


class GenFeature(Base):
    __tablename__ = 'gen_feature'

    uid = Column(Integer, primary_key=True, index=True)
    comb_key = Column(String(100), nullable=False, unique=True)
    genome_uid = Column(Integer)
    contig_index = Column(Integer)
    feature = Column(String(100))
    feature_name = Column(String(100))
    feature_index = Column(Integer)
    begin = Column(Integer)
    end = Column(Integer)
    strand = Column(String(1))
    frame = Column(Integer)
    length = Column(Integer)
    ec = Column(Text)
    go = Column(Text)
    gi = Column(Integer, nullable=False, server_default=text("'-1'"))
    function_seed = Column(Text)
    category = Column(Text)
    subcategory = Column(Text)
    subsystem = Column(Text)
    cog_id = Column(String(30))
    cog_category = Column(String(30))
    cog_gene = Column(String(50))
    cog_function = Column(Text)
    cog_evalue = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    CDD = Column(Integer, nullable=False, server_default=text("'-1'"))
    ncbi_gene_id = Column(String(30))
    ncbi_protein_id = Column(String(30))
    ncbi_product = Column(Text)
    ncbi_note = Column(Text)
    ncbi_contig_acc = Column(String(30))
    ncbi_contig_gi = Column(Integer, nullable=False, server_default=text("'-1'"))
    ncbi_gpid = Column(Integer, nullable=False, server_default=text("'-1'"))
    ncbi_gene = Column(String(100))
    dna = Column(String)
    protein = Column(Text)
    ref_feature_name = Column(String(255))
    ref_feature_sim = Column(Float(asdecimal=True), server_default=text("'-1'"))
    ref_feature_name_genus = Column(String(200, u'latin1_general_ci'))
    ref_feature_sim_genus = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    point = Column(Integer, nullable=False, server_default=text("'-1'"))
    abs_pos = Column(Integer, nullable=False, server_default=text("'-1'"))
    codon_start = Column(Integer, nullable=False, server_default=text("'1'"))
    ncbi_location = Column(Text(collation=u'latin1_general_ci'))
    go_note = Column(Text(collation=u'latin1_general_ci'))
    go_evalue = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ncbi_function = Column(Text(collation=u'latin1_general_ci'))
    ncbi_db_xref = Column(Text(collation=u'latin1_general_ci'))
    ncbi_transcript_id = Column(String(250, u'latin1_general_ci'))
    ncbi_inference = Column(String(collation=u'latin1_general_ci'))
    ncbi_ncRNA_class = Column(String(250, u'latin1_general_ci'))
    ncbi_standard_name = Column(Text(collation=u'latin1_general_ci'))
    ncbi_gene_synonym = Column(Text(collation=u'latin1_general_ci'))
    ncbi_transl_except = Column(Text(collation=u'latin1_general_ci'))
    ncbi_experiment = Column(Text(collation=u'latin1_general_ci'))
    ncbi_mobile_element = Column(Text(collation=u'latin1_general_ci'))
    ncbi_exception = Column(Text(collation=u'latin1_general_ci'))
    ncbi_map = Column(Text(collation=u'latin1_general_ci'))
    ncbi_label = Column(Text(collation=u'latin1_general_ci'))
    ncbi_replace = Column(Text(collation=u'latin1_general_ci'))
    ncbi_rpt_family = Column(Text(collation=u'latin1_general_ci'))
    ncbi_bound_moiety = Column(Text(collation=u'latin1_general_ci'))
    ncbi_rpt_unit_seq = Column(Text(collation=u'latin1_general_ci'))
    ncbi_rpt_type = Column(Text(collation=u'latin1_general_ci'))
    ncbi_rpt_unit_range = Column(Text(collation=u'latin1_general_ci'))
    ncbi_operon = Column(Text(collation=u'latin1_general_ci'))
    ncbi_direction = Column(Text(collation=u'latin1_general_ci'))
    ncbi_tag_peptide = Column(Text(collation=u'latin1_general_ci'))
    ncbi_estimated_length = Column(Text(collation=u'latin1_general_ci'))
    ncbi_allele = Column(Text(collation=u'latin1_general_ci'))
    codon_recognized = Column(Text(collation=u'latin1_general_ci'))
    anticodon = Column(Text(collation=u'latin1_general_ci'))
    old_locus_tag = Column(Text(collation=u'latin1_general_ci'))
    ncbi_others = Column(String(collation=u'latin1_general_ci'))
    number = Column(Integer, nullable=False, server_default=text("'-1'"))
    partial = Column(Integer, nullable=False, server_default=text("'0'"))
    transl_table = Column(Integer, nullable=False, server_default=text("'11'"))
    pseudo = Column(Integer, nullable=False, server_default=text("'0'"))
    ribosomal_slippage = Column(Integer, nullable=False, server_default=text("'0'"))
    trans_splicing = Column(Integer, nullable=False, server_default=text("'0'"))
    count = Column(Integer, nullable=False, server_default=text("'-1'"))
    layer = Column(Integer, server_default=text("'-1'"))


class Gene(Base):
    __tablename__ = 'gene'
    __table_args__ = (
        Index('uid_2', 'uid', 'gene'),
    )

    uid = Column(Integer, primary_key=True, unique=True)
    gene = Column(String(250), nullable=False)
    comment = Column(Text)


class Genome(Base):
    __tablename__ = 'genome'

    uid = Column(Integer, primary_key=True)
    stamp_update = Column(DateTime, nullable=False, server_default=text("'2000-01-01 00:00:00'"))
    stamp_insert = Column(DateTime, nullable=False, server_default=text("'2000-01-01 00:00:00'"))
    comment_user = Column(String)
    comment_internal = Column(String)
    user_group_uid = Column(Integer, nullable=False, server_default=text("'-1'"))
    share_with_lab = Column(Integer, nullable=False, server_default=text("'0'"))
    species = Column(String(250), nullable=False)
    prefix = Column(String(20), nullable=False)
    strain = Column(Text)
    run_uid = Column(Integer, nullable=False, server_default=text("'-1'"))
    method = Column(Integer, nullable=False, server_default=text("'0'"))
    assembler = Column(Integer, nullable=False, server_default=text("'1'"))
    genome_size = Column(Integer, nullable=False, server_default=text("'-1'"))
    gc_ratio = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    read_n = Column(Integer, nullable=False, server_default=text("'-1'"))
    read_total = Column(Integer, nullable=False, server_default=text("'-1'"))
    coverage = Column(String(10))
    N75 = Column(Integer, nullable=False, server_default=text("'-1'"))
    N50 = Column(Integer, nullable=False, server_default=text("'-1'"))
    N25 = Column(Integer, nullable=False, server_default=text("'-1'"))
    contig_n = Column(Integer, nullable=False, server_default=text("'-1'"))
    contig_stat = Column(String)
    scaffold_n = Column(Integer, server_default=text("'-1'"))
    ssu_rrn = Column(Text)
    ssu_rrn_acc = Column(Text)
    ssu_rrn_sim = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ssu_rrn_tax = Column(Text)
    ncbi_name = Column(String(250))
    ref_ncbi_gpid = Column(Integer)
    ref_ncbi_name = Column(String(250))
    share_user_group = Column(String)
    ref_ncbi_gpid_genus = Column(Integer)
    ref_ncbi_name_genus = Column(String(250))
    ref_ncbi_gpid_phylum = Column(Integer, server_default=text("'0'"))
    ref_ncbi_name_phylum = Column(String(250), server_default=text("'0'"))
    ref_ncbi_gpid_domain = Column(Integer, server_default=text("'0'"))
    ref_ncbi_name_domain = Column(String(250), server_default=text("'0'"))
    annotation_with = Column(Enum(u'na', u'contig', u'scaffold'), server_default=text("'na'"))
    status = Column(Integer, server_default=text("'0'"))
    aux_data = Column(String(250))
    figfam_id = Column(String(100))
    ann_source = Column(String(200))
    gene_cluster = Column(String(200))
    comment = Column(Text)


class GenomeComment(Base):
    __tablename__ = 'genome_comment'

    unique_id = Column(Integer, primary_key=True)
    uid = Column(Integer, nullable=False)
    created_by = Column(String(100), nullable=False)
    created_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    comment = Column(Text, nullable=False)


class GenomeContig(Base):
    __tablename__ = 'genome_contig'

    uid = Column(Integer, primary_key=True)
    comb_key = Column(String(50), nullable=False, unique=True)
    genome_uid = Column(Integer, server_default=text("'-1'"))
    seq_index = Column(Integer, server_default=text("'-1'"))
    length = Column(Integer, server_default=text("'-1'"))
    accession = Column(String(30))
    gi = Column(Integer, nullable=False, server_default=text("'-1'"))
    sequence = Column(String)
    comment = Column(Text)
    stamp_update = Column(DateTime, nullable=False, server_default=text("'2010-01-01 12:00:00'"))
    stamp_insert = Column(DateTime, nullable=False, server_default=text("'2010-01-01 12:00:00'"))
    mol_type = Column(Integer, server_default=text("'3'"))
    mol_shape = Column(String(100))


class GenomeContigCopy(Base):
    __tablename__ = 'genome_contig_copy'

    uid = Column(Integer, primary_key=True)
    comb_key = Column(String(50), nullable=False, unique=True)
    genome_uid = Column(Integer, server_default=text("'-1'"))
    seq_index = Column(Integer, server_default=text("'-1'"))
    length = Column(Integer, server_default=text("'-1'"))
    accession = Column(String(30))
    gi = Column(Integer, nullable=False, server_default=text("'-1'"))
    sequence = Column(String)
    comment = Column(Text)
    stamp_update = Column(DateTime, nullable=False, server_default=text("'2010-01-01 12:00:00'"))
    stamp_insert = Column(DateTime, nullable=False, server_default=text("'2010-01-01 12:00:00'"))
    mol_type = Column(Integer)
    mol_shape = Column(String(100))


class GenomeCopy(Base):
    __tablename__ = 'genome_copy'

    uid = Column(Integer, primary_key=True)
    stamp_update = Column(DateTime, nullable=False, server_default=text("'2000-01-01 00:00:00'"))
    stamp_insert = Column(DateTime, nullable=False, server_default=text("'2000-01-01 00:00:00'"))
    comment_user = Column(String)
    comment_internal = Column(String)
    user_group_uid = Column(Integer, nullable=False, server_default=text("'-1'"))
    share_with_lab = Column(Integer, nullable=False, server_default=text("'0'"))
    species = Column(String(250), nullable=False)
    prefix = Column(String(20), nullable=False)
    strain = Column(Text)
    run_uid = Column(Integer, nullable=False, server_default=text("'-1'"))
    method = Column(Integer, nullable=False, server_default=text("'0'"))
    assembler = Column(Integer, nullable=False, server_default=text("'1'"))
    genome_size = Column(Integer, nullable=False, server_default=text("'-1'"))
    gc_ratio = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    read_n = Column(Integer, nullable=False, server_default=text("'-1'"))
    read_total = Column(Integer, nullable=False, server_default=text("'-1'"))
    coverage = Column(String(10))
    N75 = Column(Integer, nullable=False, server_default=text("'-1'"))
    N50 = Column(Integer, nullable=False, server_default=text("'-1'"))
    N25 = Column(Integer, nullable=False, server_default=text("'-1'"))
    contig_n = Column(Integer, nullable=False, server_default=text("'-1'"))
    contig_stat = Column(String)
    scaffold_n = Column(Integer, server_default=text("'-1'"))
    ssu_rrn = Column(Text)
    ssu_rrn_acc = Column(Text)
    ssu_rrn_sim = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ssu_rrn_tax = Column(Text)
    ncbi_name = Column(String(250))
    ref_ncbi_gpid = Column(Integer)
    ref_ncbi_name = Column(String(250))
    share_user_group = Column(String)
    ref_ncbi_gpid_genus = Column(Integer)
    ref_ncbi_name_genus = Column(String(250))
    ref_ncbi_gpid_phylum = Column(Integer, server_default=text("'0'"))
    ref_ncbi_name_phylum = Column(String(250), server_default=text("'0'"))
    ref_ncbi_gpid_domain = Column(Integer, server_default=text("'0'"))
    ref_ncbi_name_domain = Column(String(250), server_default=text("'0'"))
    annotation_with = Column(Enum(u'na', u'contig', u'scaffold'), server_default=text("'na'"))
    status = Column(Integer, server_default=text("'0'"))
    aux_data = Column(String(250))


class GenomeFeature(Base):
    __tablename__ = 'genome_feature'

    uid = Column(Integer, primary_key=True, index=True)
    comb_key = Column(String(100), nullable=False, unique=True)
    genome_uid = Column(Integer)
    contig_index = Column(Integer)
    feature = Column(String(100))
    feature_name = Column(String(100))
    feature_index = Column(Integer)
    begin = Column(Integer)
    end = Column(Integer)
    strand = Column(String(1))
    frame = Column(Integer)
    length = Column(Integer)
    ec = Column(Text)
    go = Column(Text)
    gi = Column(Integer, nullable=False, server_default=text("'-1'"))
    function_seed = Column(Text)
    category = Column(Text)
    subcategory = Column(Text)
    subsystem = Column(Text)
    cog_id = Column(String(30))
    cog_category = Column(String(30))
    cog_gene = Column(String(50))
    cog_function = Column(Text)
    cog_evalue = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    CDD = Column(Integer, nullable=False, server_default=text("'-1'"))
    ncbi_gene_id = Column(String(30))
    ncbi_protein_id = Column(String(30))
    ncbi_product = Column(Text)
    ncbi_note = Column(Text)
    ncbi_contig_acc = Column(String(30))
    ncbi_contig_gi = Column(Integer, nullable=False, server_default=text("'-1'"))
    ncbi_gpid = Column(Integer, nullable=False, server_default=text("'-1'"))
    ncbi_gene = Column(String(100))
    dna = Column(String)
    protein = Column(Text)
    ref_feature_name = Column(String(255))
    ref_feature_sim = Column(Float(asdecimal=True), server_default=text("'-1'"))
    ref_feature_name_genus = Column(String(200, u'latin1_general_ci'))
    ref_feature_sim_genus = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ref_feature_name_phylum = Column(String(200), nullable=False, server_default=text("'-1'"))
    ref_feature_sim_phylum = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ref_feature_name_domain = Column(String(200), nullable=False, server_default=text("'-1'"))
    ref_feature_sim_domain = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    point = Column(Integer, nullable=False, server_default=text("'-1'"))
    abs_pos = Column(Integer, nullable=False, server_default=text("'-1'"))
    codon_start = Column(Integer, nullable=False, server_default=text("'1'"))
    ncbi_location = Column(Text(collation=u'latin1_general_ci'))
    go_note = Column(Text(collation=u'latin1_general_ci'))
    go_evalue = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ncbi_function = Column(Text(collation=u'latin1_general_ci'))
    ncbi_db_xref = Column(Text(collation=u'latin1_general_ci'))
    ncbi_transcript_id = Column(String(250, u'latin1_general_ci'))
    ncbi_inference = Column(String(collation=u'latin1_general_ci'))
    ncbi_ncRNA_class = Column(String(250, u'latin1_general_ci'))
    ncbi_standard_name = Column(Text(collation=u'latin1_general_ci'))
    ncbi_gene_synonym = Column(Text(collation=u'latin1_general_ci'))
    ncbi_transl_except = Column(Text(collation=u'latin1_general_ci'))
    ncbi_experiment = Column(Text(collation=u'latin1_general_ci'))
    ncbi_mobile_element = Column(Text(collation=u'latin1_general_ci'))
    ncbi_exception = Column(Text(collation=u'latin1_general_ci'))
    ncbi_map = Column(Text(collation=u'latin1_general_ci'))
    ncbi_label = Column(Text(collation=u'latin1_general_ci'))
    ncbi_replace = Column(Text(collation=u'latin1_general_ci'))
    ncbi_rpt_family = Column(Text(collation=u'latin1_general_ci'))
    ncbi_bound_moiety = Column(Text(collation=u'latin1_general_ci'))
    ncbi_rpt_unit_seq = Column(Text(collation=u'latin1_general_ci'))
    ncbi_rpt_type = Column(Text(collation=u'latin1_general_ci'))
    ncbi_rpt_unit_range = Column(Text(collation=u'latin1_general_ci'))
    ncbi_operon = Column(Text(collation=u'latin1_general_ci'))
    ncbi_direction = Column(Text(collation=u'latin1_general_ci'))
    ncbi_tag_peptide = Column(Text(collation=u'latin1_general_ci'))
    ncbi_estimated_length = Column(Text(collation=u'latin1_general_ci'))
    ncbi_allele = Column(Text(collation=u'latin1_general_ci'))
    codon_recognized = Column(Text(collation=u'latin1_general_ci'))
    anticodon = Column(Text(collation=u'latin1_general_ci'))
    old_locus_tag = Column(Text(collation=u'latin1_general_ci'))
    ncbi_others = Column(String(collation=u'latin1_general_ci'))
    number = Column(Integer, nullable=False, server_default=text("'-1'"))
    partial = Column(Integer, nullable=False, server_default=text("'0'"))
    transl_table = Column(Integer, nullable=False, server_default=text("'11'"))
    pseudo = Column(Integer, nullable=False, server_default=text("'0'"))
    ribosomal_slippage = Column(Integer, nullable=False, server_default=text("'0'"))
    trans_splicing = Column(Integer, nullable=False, server_default=text("'0'"))
    count = Column(Integer, nullable=False, server_default=text("'-1'"))
    layer = Column(Integer, server_default=text("'-1'"))
    feature_version = Column(Integer, server_default=text("'0'"))


class GenomeFeatureCopy(Base):
    __tablename__ = 'genome_feature_copy'

    uid = Column(Integer, primary_key=True, index=True)
    comb_key = Column(String(100), nullable=False, unique=True)
    genome_uid = Column(Integer)
    contig_index = Column(Integer)
    feature = Column(String(100))
    feature_name = Column(String(100))
    feature_index = Column(Integer)
    begin = Column(Integer)
    end = Column(Integer)
    strand = Column(String(1))
    frame = Column(Integer)
    length = Column(Integer)
    ec = Column(Text)
    go = Column(Text)
    gi = Column(Integer, nullable=False, server_default=text("'-1'"))
    function_seed = Column(Text)
    category = Column(Text)
    subcategory = Column(Text)
    subsystem = Column(Text)
    cog_id = Column(String(30))
    cog_category = Column(String(30))
    cog_gene = Column(String(50))
    cog_function = Column(Text)
    cog_evalue = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    CDD = Column(Integer, nullable=False, server_default=text("'-1'"))
    ncbi_gene_id = Column(String(30))
    ncbi_protein_id = Column(String(30))
    ncbi_product = Column(Text)
    ncbi_note = Column(Text)
    ncbi_contig_acc = Column(String(30))
    ncbi_contig_gi = Column(Integer, nullable=False, server_default=text("'-1'"))
    ncbi_gpid = Column(Integer, nullable=False, server_default=text("'-1'"))
    ncbi_gene = Column(String(100))
    dna = Column(String)
    protein = Column(Text)
    ref_feature_name = Column(String(255))
    ref_feature_sim = Column(Float(asdecimal=True), server_default=text("'-1'"))
    ref_feature_name_genus = Column(String(200, u'latin1_general_ci'))
    ref_feature_sim_genus = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ref_feature_name_phylum = Column(String(200), nullable=False, server_default=text("'-1'"))
    ref_feature_sim_phylum = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ref_feature_name_domain = Column(String(200), nullable=False, server_default=text("'-1'"))
    ref_feature_sim_domain = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    point = Column(Integer, nullable=False, server_default=text("'-1'"))
    abs_pos = Column(Integer, nullable=False, server_default=text("'-1'"))
    codon_start = Column(Integer, nullable=False, server_default=text("'1'"))
    ncbi_location = Column(Text(collation=u'latin1_general_ci'))
    go_note = Column(Text(collation=u'latin1_general_ci'))
    go_evalue = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ncbi_function = Column(Text(collation=u'latin1_general_ci'))
    ncbi_db_xref = Column(Text(collation=u'latin1_general_ci'))
    ncbi_transcript_id = Column(String(250, u'latin1_general_ci'))
    ncbi_inference = Column(String(collation=u'latin1_general_ci'))
    ncbi_ncRNA_class = Column(String(250, u'latin1_general_ci'))
    ncbi_standard_name = Column(Text(collation=u'latin1_general_ci'))
    ncbi_gene_synonym = Column(Text(collation=u'latin1_general_ci'))
    ncbi_transl_except = Column(Text(collation=u'latin1_general_ci'))
    ncbi_experiment = Column(Text(collation=u'latin1_general_ci'))
    ncbi_mobile_element = Column(Text(collation=u'latin1_general_ci'))
    ncbi_exception = Column(Text(collation=u'latin1_general_ci'))
    ncbi_map = Column(Text(collation=u'latin1_general_ci'))
    ncbi_label = Column(Text(collation=u'latin1_general_ci'))
    ncbi_replace = Column(Text(collation=u'latin1_general_ci'))
    ncbi_rpt_family = Column(Text(collation=u'latin1_general_ci'))
    ncbi_bound_moiety = Column(Text(collation=u'latin1_general_ci'))
    ncbi_rpt_unit_seq = Column(Text(collation=u'latin1_general_ci'))
    ncbi_rpt_type = Column(Text(collation=u'latin1_general_ci'))
    ncbi_rpt_unit_range = Column(Text(collation=u'latin1_general_ci'))
    ncbi_operon = Column(Text(collation=u'latin1_general_ci'))
    ncbi_direction = Column(Text(collation=u'latin1_general_ci'))
    ncbi_tag_peptide = Column(Text(collation=u'latin1_general_ci'))
    ncbi_estimated_length = Column(Text(collation=u'latin1_general_ci'))
    ncbi_allele = Column(Text(collation=u'latin1_general_ci'))
    codon_recognized = Column(Text(collation=u'latin1_general_ci'))
    anticodon = Column(Text(collation=u'latin1_general_ci'))
    old_locus_tag = Column(Text(collation=u'latin1_general_ci'))
    ncbi_others = Column(String(collation=u'latin1_general_ci'))
    number = Column(Integer, nullable=False, server_default=text("'-1'"))
    partial = Column(Integer, nullable=False, server_default=text("'0'"))
    transl_table = Column(Integer, nullable=False, server_default=text("'11'"))
    pseudo = Column(Integer, nullable=False, server_default=text("'0'"))
    ribosomal_slippage = Column(Integer, nullable=False, server_default=text("'0'"))
    trans_splicing = Column(Integer, nullable=False, server_default=text("'0'"))
    count = Column(Integer, nullable=False, server_default=text("'-1'"))
    layer = Column(Integer, server_default=text("'-1'"))
    feature_version = Column(Integer, server_default=text("'0'"))


class GenomeI(Base):
    __tablename__ = 'genome_i'

    uid = Column(Integer, primary_key=True)
    user_group_uid = Column(Integer, nullable=False, server_default=text("'-1'"))
    project_type = Column(Integer, nullable=False, server_default=text("'0'"))
    species = Column(String(200))
    sample_name = Column(String(200))
    sample_received_date = Column(Date)
    illumina_status = Column(Integer, nullable=False, server_default=text("'0'"))
    _454_status = Column('454_status', Integer, nullable=False, server_default=text("'0'"))
    n_scaffolds = Column(Integer, nullable=False, server_default=text("'-1'"))
    n_contigs = Column(Integer, nullable=False, server_default=text("'-1'"))
    n_gaps = Column(Integer, nullable=False, server_default=text("'-1'"))
    comment_market = Column(Text)


class GenomeMethod(Base):
    __tablename__ = 'genome_method'

    uid = Column(Integer, primary_key=True)
    method = Column(String(250))
    comment = Column(Text)


class GenomeProjectType(Base):
    __tablename__ = 'genome_project_type'

    uid = Column(Integer, primary_key=True)
    content = Column(String(250), nullable=False)
    comment = Column(Text)


class GenomeScaffold(Base):
    __tablename__ = 'genome_scaffold'

    uid = Column(Integer, primary_key=True)
    comb_key = Column(String(50), nullable=False, unique=True)
    genome_uid = Column(Integer, server_default=text("'-1'"))
    seq_index = Column(Integer, server_default=text("'-1'"))
    length = Column(Integer, server_default=text("'-1'"))
    contig_info = Column(Text)
    sequence = Column(String)
    comment = Column(Text)
    mol_type = Column(Integer, server_default=text("'4'"))
    accession = Column(String(30))
    stamp_update = Column(DateTime, nullable=False, server_default=text("'2010-01-01 12:00:00'"))
    stamp_insert = Column(DateTime, nullable=False, server_default=text("'2010-01-01 12:00:00'"))


class GenomeScaffoldCopy(Base):
    __tablename__ = 'genome_scaffold_copy'

    uid = Column(Integer, primary_key=True)
    comb_key = Column(String(50), nullable=False, unique=True)
    genome_uid = Column(Integer, server_default=text("'-1'"))
    seq_index = Column(Integer, server_default=text("'-1'"))
    length = Column(Integer, server_default=text("'-1'"))
    contig_info = Column(Text)
    sequence = Column(String)
    comment = Column(Text)
    mol_type = Column(Integer, server_default=text("'0'"))
    accession = Column(String(30))
    stamp_update = Column(DateTime, nullable=False, server_default=text("'2010-01-01 12:00:00'"))
    stamp_insert = Column(DateTime, nullable=False, server_default=text("'2010-01-01 12:00:00'"))


class Job(Base):
    __tablename__ = 'job'

    uid = Column(Integer, primary_key=True)
    command = Column(String)
    priority = Column(Integer, server_default=text("'0'"))
    stamp_start = Column(DateTime)
    stamp_finish = Column(DateTime)
    worker = Column(String(50))
    error = Column(Text)
    comment = Column(Text)
    worker_allow = Column(String(250))
    name = Column(String(250))
    schedule_uid = Column(Integer, server_default=text("'-1'"))
    is_terminated = Column(Integer, server_default=text("'0'"))
    obj_uid = Column(Integer)
    run_uid = Column(Integer)


class Metagenome(Base):
    __tablename__ = 'metagenome'

    uid = Column(Integer, primary_key=True)
    stamp_update = Column(DateTime, nullable=False, server_default=text("'2000-01-01 00:00:00'"))
    stamp_insert = Column(DateTime, nullable=False, server_default=text("'2000-01-01 00:00:00'"))
    comment_user = Column(String)
    comment_internal = Column(String)
    user_group_uid = Column(Integer, nullable=False, server_default=text("'-1'"))
    user_sample_name = Column(String(250), nullable=False)
    sample_description = Column(Text)
    run_uid = Column(Integer, server_default=text("'-1'"))
    machine_id = Column(Integer, server_default=text("'-1'"))
    n_reads = Column(Integer, server_default=text("'-1'"))
    read_avg = Column(Float(asdecimal=True), server_default=text("'-1'"))
    read_min = Column(Integer, server_default=text("'-1'"))
    read_max = Column(Integer, server_default=text("'-1'"))
    qual_avg = Column(Integer, server_default=text("'-1'"))
    read_len_total = Column(Integer, server_default=text("'-1'"))
    n_contigs = Column(Integer, server_default=text("'-1'"))
    contig_avg = Column(Float(asdecimal=True), server_default=text("'-1'"))
    contig_max = Column(Integer, server_default=text("'-1'"))
    contig_min = Column(Integer, server_default=text("'-1'"))
    contig_len_total = Column(Integer, server_default=text("'-1'"))
    read_done = Column(Integer, server_default=text("'-1'"))
    contig_done = Column(Integer, server_default=text("'-1'"))
    megan_nr_done = Column(Integer, server_default=text("'-1'"))
    megan_nt_done = Column(Integer, server_default=text("'-1'"))
    n_reads_blast = Column(Integer)
    blast_done = Column(Integer, server_default=text("'-1'"))
    n_ssu = Column(Integer, server_default=text("'-1'"))


class NcbiGenomeFeature(Base):
    __tablename__ = 'ncbi_genome_feature'

    uid = Column(Integer, primary_key=True, index=True)
    comb_key = Column(String(200, u'latin1_general_ci'), nullable=False, unique=True)
    genome_uid = Column(Integer, index=True)
    contig_index = Column(Integer, nullable=False)
    feature = Column(String(100, u'latin1_general_ci'), index=True)
    feature_name = Column(String(200, u'latin1_general_ci'), index=True)
    feature_index = Column(Integer, index=True)
    ref_feature_name = Column(String(200, u'latin1_general_ci'))
    ref_feature_sim = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ref_feature_name_genus = Column(String(200, u'latin1_general_ci'))
    ref_feature_sim_genus = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    begin = Column(Integer, nullable=False, server_default=text("'-1'"))
    end = Column(Integer, nullable=False, server_default=text("'-1'"))
    point = Column(Integer, nullable=False, server_default=text("'-1'"))
    abs_pos = Column(Integer, nullable=False, server_default=text("'-1'"))
    codon_start = Column(Integer, nullable=False, server_default=text("'1'"))
    ncbi_location = Column(Text(collation=u'latin1_general_ci'))
    strand = Column(String(1, u'latin1_general_ci'))
    frame = Column(Integer, nullable=False, server_default=text("'-1'"))
    length = Column(Integer, nullable=False, server_default=text("'-1'"))
    ec = Column(Text(collation=u'latin1_general_ci'))
    go = Column(Text(collation=u'latin1_general_ci'))
    go_note = Column(Text(collation=u'latin1_general_ci'))
    go_evalue = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    gi = Column(Integer, nullable=False, server_default=text("'-1'"))
    function_seed = Column(Text(collation=u'latin1_general_ci'))
    category = Column(Text(collation=u'latin1_general_ci'))
    subcategory = Column(Text(collation=u'latin1_general_ci'))
    subsystem = Column(Text(collation=u'latin1_general_ci'))
    cog_id = Column(String(30, u'latin1_general_ci'))
    cog_category = Column(String(30, u'latin1_general_ci'))
    cog_gene = Column(String(50, u'latin1_general_ci'))
    cog_function = Column(Text(collation=u'latin1_general_ci'))
    cog_evalue = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    CDD = Column(Integer, nullable=False, server_default=text("'-1'"))
    ncbi_gene_id = Column(String(30, u'latin1_general_ci'))
    ncbi_protein_id = Column(String(30, u'latin1_general_ci'))
    ncbi_product = Column(Text(collation=u'latin1_general_ci'))
    ncbi_note = Column(String(collation=u'latin1_general_ci'))
    ncbi_contig_acc = Column(String(30, u'latin1_general_ci'), index=True)
    ncbi_contig_gi = Column(Integer, nullable=False, server_default=text("'-1'"))
    ncbi_gpid = Column(Integer, nullable=False, index=True, server_default=text("'-1'"))
    ncbi_gene = Column(String(100, u'latin1_general_ci'))
    ncbi_function = Column(Text(collation=u'latin1_general_ci'))
    ncbi_db_xref = Column(Text(collation=u'latin1_general_ci'))
    ncbi_transcript_id = Column(String(250, u'latin1_general_ci'))
    ncbi_inference = Column(String(collation=u'latin1_general_ci'))
    ncbi_ncRNA_class = Column(String(250, u'latin1_general_ci'))
    ncbi_standard_name = Column(Text(collation=u'latin1_general_ci'))
    ncbi_gene_synonym = Column(Text(collation=u'latin1_general_ci'))
    ncbi_transl_except = Column(Text(collation=u'latin1_general_ci'))
    ncbi_experiment = Column(Text(collation=u'latin1_general_ci'))
    ncbi_mobile_element = Column(Text(collation=u'latin1_general_ci'))
    ncbi_exception = Column(Text(collation=u'latin1_general_ci'))
    ncbi_map = Column(Text(collation=u'latin1_general_ci'))
    ncbi_label = Column(Text(collation=u'latin1_general_ci'))
    ncbi_replace = Column(Text(collation=u'latin1_general_ci'))
    ncbi_rpt_family = Column(Text(collation=u'latin1_general_ci'))
    ncbi_bound_moiety = Column(Text(collation=u'latin1_general_ci'))
    ncbi_rpt_unit_seq = Column(Text(collation=u'latin1_general_ci'))
    ncbi_rpt_type = Column(Text(collation=u'latin1_general_ci'))
    ncbi_rpt_unit_range = Column(Text(collation=u'latin1_general_ci'))
    ncbi_operon = Column(Text(collation=u'latin1_general_ci'))
    ncbi_direction = Column(Text(collation=u'latin1_general_ci'))
    ncbi_tag_peptide = Column(Text(collation=u'latin1_general_ci'))
    ncbi_estimated_length = Column(Text(collation=u'latin1_general_ci'))
    ncbi_allele = Column(Text(collation=u'latin1_general_ci'))
    codon_recognized = Column(Text(collation=u'latin1_general_ci'))
    anticodon = Column(Text(collation=u'latin1_general_ci'))
    old_locus_tag = Column(Text(collation=u'latin1_general_ci'))
    ncbi_others = Column(String(collation=u'latin1_general_ci'))
    number = Column(Integer, nullable=False, server_default=text("'-1'"))
    partial = Column(Integer, nullable=False, server_default=text("'0'"))
    transl_table = Column(Integer, nullable=False, server_default=text("'11'"))
    pseudo = Column(Integer, nullable=False, server_default=text("'0'"))
    ribosomal_slippage = Column(Integer, nullable=False, server_default=text("'0'"))
    trans_splicing = Column(Integer, nullable=False, server_default=text("'0'"))
    count = Column(Integer, nullable=False, server_default=text("'-1'"))
    dna = Column(String(collation=u'latin1_general_ci'))
    protein = Column(Text(collation=u'latin1_general_ci'))


class Order(Base):
    __tablename__ = 'orders'

    uid = Column(Integer, primary_key=True, unique=True)
    owner_user_group_uid = Column(Integer, nullable=False, server_default=text("'0'"))
    title = Column(String(255), nullable=False, server_default=text("''"))
    status = Column(String(20), nullable=False, server_default=text("''"))
    stamp_insert = Column(DateTime, nullable=False, server_default=text("'2010-01-01 00:00:00'"))
    stamp_update = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP"))


class Pfid(Base):
    __tablename__ = 'pfid'
    __table_args__ = (
        Index('idx', 'service', 'service_detail', unique=True),
    )

    uid = Column(Integer, primary_key=True)
    service = Column(String(1), nullable=False)
    service_detail = Column(String(1))
    pfid = Column(Integer, nullable=False, server_default=text("'1'"))


class PrimerSet(Base):
    __tablename__ = 'primer_set'

    uid = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    ngs = Column(String(50), nullable=False)
    is_paired_end = Column(Integer, nullable=False, server_default=text("'0'"))
    raw_type = Column(Enum(u'sff', u'fasta', u'fastq', u'FQ'), server_default=text("'sff'"))
    target = Column(String(50), nullable=False)
    for_name = Column(String(50), nullable=False)
    for_seq = Column(String(50), nullable=False)
    for_position = Column(Integer, nullable=False, server_default=text("'-1'"))
    rev_name = Column(String(50), nullable=False)
    rev_seq = Column(String(50), nullable=False)
    rev_position = Column(Integer, nullable=False, server_default=text("'-1'"))
    direction = Column(String(1), nullable=False, server_default=text("'r'"))
    trim_primer_run = Column(Integer, nullable=False, server_default=text("'1'"))
    trim_hmm_run = Column(Integer, nullable=False, server_default=text("'0'"))
    trim_hmm_filename = Column(String(200))
    assembly_run = Column(Integer, nullable=False, server_default=text("'0'"))
    assembly_mismatch_allow = Column(Integer, server_default=text("'2'"))
    chimera_run = Column(Integer, nullable=False, server_default=text("'0'"))
    chimera_filename = Column(String(200))
    assign_filename = Column(String(200), nullable=False)
    reference = Column(Text)
    comment = Column(Text)


class Rnaseq(Base):
    __tablename__ = 'rnaseq'

    uid = Column(Integer, primary_key=True)
    stamp_update = Column(DateTime, nullable=False, server_default=text("'2000-01-01 00:00:00'"))
    stamp_insert = Column(DateTime, nullable=False, server_default=text("'2000-01-01 00:00:00'"))
    comment_user = Column(String)
    comment_internal = Column(String)
    user_group_uid = Column(Integer, nullable=False, server_default=text("'-1'"))
    share_with_lab = Column(Integer, nullable=False, server_default=text("'0'"))
    share_user_group = Column(String)
    species = Column(String(250), nullable=False)
    strain = Column(Text)
    mapped_by = Column(String(100))
    run_uid = Column(Integer, nullable=False, server_default=text("'-1'"))
    method = Column(Integer, nullable=False, server_default=text("'0'"))
    n_read_length = Column(Integer)
    n_read = Column(Integer)
    n_read_total = Column(Integer)
    d_coverage = Column(Float(asdecimal=True))
    ref_ncbi_gpid = Column(Integer)
    ref_ncbi_name = Column(String(250))
    ref_genome_size = Column(Integer, nullable=False, server_default=text("'-1'"))
    n_chromosome = Column(Integer)
    n_plasmid = Column(Integer)
    n_contig = Column(Integer)
    meta_experiment = Column(String)
    n_mapped_read = Column(Integer)
    n_read_cds = Column(Integer)
    n_read_rrna = Column(Integer)
    n_read_trna = Column(Integer)
    d_avg_depth = Column(Float(11, True))
    d_cds_ratio = Column(Float(11, True))
    d_rrna_ratio = Column(Float(11, True))
    d_trna_ratio = Column(Float(11, True))


class RnaseqContig(Base):
    __tablename__ = 'rnaseq_contig'

    uid = Column(Integer, primary_key=True)
    stamp_insert = Column(DateTime, nullable=False, server_default=text("'2000-01-01 12:00:00'"))
    stamp_update = Column(DateTime, nullable=False, server_default=text("'2000-01-01 12:00:00'"))
    rnaseq_uid = Column(Integer, nullable=False)
    accession = Column(String(100), nullable=False)
    depth = Column(String, nullable=False)
    rpkm = Column(String, nullable=False)
    n_contig_length = Column(Integer)
    n_mapped_reads = Column(Integer)
    d_coverage = Column(Float(asdecimal=True))
    d_avg_depth = Column(Float(11, True))
    n_cds = Column(Integer)
    n_rrna = Column(Integer)
    n_trna = Column(Integer)
    n_read_cds = Column(Integer)
    n_read_rrna = Column(Integer)
    n_read_trna = Column(Integer)
    d_ratio_cds = Column(Float(11, True))
    d_ratio_rrna = Column(Float(11, True))
    d_ratio_trna = Column(Float(11, True))


class RnaseqProfile(Base):
    __tablename__ = 'rnaseq_profile'

    pfid = Column(String(50), primary_key=True)
    reference = Column(String(100), nullable=False)
    read_count_profile = Column(MEDIUMBLOB, nullable=False)
    rpkm_profile = Column(MEDIUMBLOB, nullable=False)
    tpm_profile = Column(MEDIUMBLOB, nullable=False)


class Run(Base):
    __tablename__ = 'run'

    uid = Column(Integer, primary_key=True)
    stamp_update = Column(DateTime, nullable=False, server_default=text("'2000-01-01 12:00:00'"))
    stamp_insert = Column(DateTime, nullable=False, server_default=text("'2000-01-01 12:00:00'"))
    comment_user = Column(String)
    comment_internal = Column(String)
    job_uid = Column(Integer)
    run_type = Column(String(30), server_default=text("'Community'"))
    owner_uid = Column(Integer, nullable=False)
    sample_type_id = Column(Integer, nullable=False)
    machine_id = Column(Integer, nullable=False)
    sequenced_by = Column(String(250))
    run_date = Column(Date)
    n_reads = Column(Integer)
    min_len = Column(Integer)
    max_len = Column(Integer)
    average_len = Column(Float(asdecimal=True))
    n_barcode_drop = Column(Integer, server_default=text("'-1'"))
    n_unqualified_reads = Column(Integer, server_default=text("'-1'"))
    n_unsorted_reads = Column(Integer, server_default=text("'-1'"))
    barcode = Column(Text)
    length_stat = Column(String)
    n_samples = Column(Integer, server_default=text("'-1'"))
    n_samples_reads = Column(Integer, server_default=text("'-1'"))
    n_samples_avg = Column(Float(asdecimal=True), server_default=text("'-1'"))
    is_updated = Column(String(1), server_default=text("'N'"))
    is_deprecated = Column(Integer, server_default=text("'0'"))
    is_processed = Column(Integer, server_default=text("'1'"))
    is_under_processing = Column(Integer, nullable=False, server_default=text("'0'"))
    is_start = Column(Integer, nullable=False, server_default=text("'0'"))
    f_abrogation = Column(String(1), server_default=text("'N'"))
    f_is_barcode_updated = Column(String(1), server_default=text("'N'"))
    ezpipeline_file_path = Column(String(255), server_default=text("'N'"))
    pfid = Column(String(50))


class RunBarcode(Base):
    __tablename__ = 'run_barcode'

    uid = Column(Integer, primary_key=True)
    f_barcode_name = Column(String(50), server_default=text("''"))
    f_barcode = Column(String(50), nullable=False, server_default=text("''"))
    f_for_linker = Column(String(5), nullable=False, server_default=text("''"))
    f_for_primer = Column(String(50), server_default=text("''"))
    f_rev_linker = Column(String(5), server_default=text("''"))
    f_rev_primer = Column(String(50), server_default=text("''"))
    f_gene = Column(String(50), server_default=text("''"))
    f_target_taxon = Column(String(50), server_default=text("''"))
    f_machine = Column(String(50), server_default=text("''"))
    f_set = Column(String(5), server_default=text("''"))


class RunForeignBarcode(Base):
    __tablename__ = 'run_foreign_barcode'

    uid = Column(Integer, primary_key=True)
    f_barcode_name = Column(String(255), server_default=text("''"))
    f_barcode = Column(String(255), server_default=text("''"))
    f_for_linker = Column(String(5), server_default=text("''"))
    f_for_primer = Column(String(255), server_default=text("''"))
    f_rev_linker = Column(String(5), server_default=text("''"))
    f_rev_primer = Column(String(255), server_default=text("''"))
    f_gene = Column(String(50), server_default=text("''"))
    f_target_taxon = Column(String(50), server_default=text("''"))
    f_machine = Column(String(50), server_default=text("''"))
    f_set = Column(String(5), server_default=text("''"))


class RunLog(Base):
    __tablename__ = 'run_log'

    uid = Column(Integer, primary_key=True)
    f_userID = Column(String(50), index=True)
    f_created = Column(DateTime, index=True, server_default=text("CURRENT_TIMESTAMP"))
    f_key = Column(String(100), index=True)
    f_value = Column(Text)
    f_run_id = Column(Integer, nullable=False, server_default=text("'-1'"))
    f_barcode = Column(Text)


class RunSample(Base):
    __tablename__ = 'run_samples'

    uid = Column(Integer, primary_key=True)
    f_run_id = Column(Integer, nullable=False, server_default=text("'-1'"))
    f_sample_id = Column(String(100), server_default=text("''"))
    f_barcode_id = Column(String(50), server_default=text("''"))
    f_taxon = Column(String(1), server_default=text("''"))
    f_flowcell = Column(String(50), server_default=text("''"))
    f_lane = Column(Integer, server_default=text("'-1'"))
    f_is_foreign = Column(String(1), server_default=text("'N'"))


class RunSamplesAbrogation(Base):
    __tablename__ = 'run_samples_abrogation'

    uid = Column(Integer, primary_key=True)
    f_run_id = Column(Integer, nullable=False, server_default=text("'-1'"))
    f_sample_id = Column(String(100), server_default=text("''"))
    f_barcode_id = Column(String(50), server_default=text("''"))
    f_taxon = Column(String(1), server_default=text("''"))
    f_flowcell = Column(String(50), server_default=text("''"))
    f_lane = Column(Integer, server_default=text("'-1'"))
    f_is_foreign = Column(String(1), server_default=text("'N'"))


class RunStatu(Base):
    __tablename__ = 'run_status'

    uid = Column(Integer, primary_key=True)
    content = Column(String(200), nullable=False)
    comment = Column(Text)


t_samples = Table(
    'samples', metadata,
    Column('uid', Integer, nullable=False, unique=True)
)


class ScheduleHistory(Base):
    __tablename__ = 'schedule_history'

    uid = Column(Integer, primary_key=True)
    pipeline = Column(String(30))
    request_id = Column(Integer, nullable=False, server_default=text("'1'"))
    user = Column(String(500))
    status = Column(String(15))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP"))
    elapse_time = Column(Float(asdecimal=True))
    run_id = Column(String(20))
    run_name = Column(String(300))
    project_yn = Column(String(1))
    mode = Column(String(1))
    sample_id = Column(String(20))
    sample_name = Column(String(100))
    sample_desc = Column(Text)
    current_job = Column(String(30))
    job_command = Column(String(300))
    job_output = Column(String)
    job_outpath = Column(String(300))
    filepath = Column(String(1000))
    job_id = Column(String(20))
    grid_yn = Column(String(1))
    grid_queue = Column(String(30))
    grid_hostname = Column(String(50))
    grid_cpu = Column(String(50))
    grid_memory = Column(String(50))
    grid_io = Column(String(50))
    error_message = Column(Text)
    error_stacktrace = Column(Text)


t_tax_group = Table(
    'tax_group', metadata,
    Column('uid', Integer),
    Column('group_name', String(250)),
    Column('tax_list', Text)
)


class TblCg(Base):
    __tablename__ = 'tbl_cg'

    uid = Column(Integer, primary_key=True)
    f_order_uid = Column(Integer, index=True, server_default=text("'-1'"))
    f_sample_id = Column(String(10), server_default=text("''"))
    f_completion_date = Column(DateTime, index=True, server_default=text("CURRENT_TIMESTAMP"))
    f_sample_guids = Column(Text)
    f_sample_numbers = Column(String(10))
    f_download = Column(Text)
    f_download_old = Column(Text)
    f_my_comment = Column(Text)
    f_admin_comment = Column(Text)
    user_group_uid = Column(Integer, server_default=text("'-1'"))
    user_uid = Column(Integer, server_default=text("'-1'"))
    share_user_uid = Column(String(500), server_default=text("'-1'"))


class TblCommDown(Base):
    __tablename__ = 'tbl_comm_down'

    uid = Column(Integer, primary_key=True)
    f_name = Column(String(200), server_default=text("''"))
    f_email = Column(String(200), server_default=text("''"))
    f_date = Column(String(50), server_default=text("''"))
    f_data_type = Column(String(50), server_default=text("''"))
    f_sample_id = Column(String(250), server_default=text("''"))


class TblGenome(Base):
    __tablename__ = 'tbl_genome'

    uid = Column(Integer, primary_key=True)
    f_order_uid = Column(Integer, index=True, server_default=text("'-1'"))
    f_sample_id = Column(String(10), index=True, server_default=text("''"))
    f_completion_date = Column(DateTime, index=True, server_default=text("CURRENT_TIMESTAMP"))
    f_species = Column(String(100), server_default=text("''"))
    f_strain = Column(String(50), server_default=text("''"))
    f_contigs = Column(Integer)
    f_size = Column(Integer)
    f_download = Column(Text)
    f_download_old = Column(Text)
    f_my_comment = Column(Text)
    f_admin_comment = Column(Text)
    user_group_uid = Column(Integer, server_default=text("'-1'"))
    user_uid = Column(Integer, server_default=text("'-1'"))
    share_user_uid = Column(String(500), server_default=text("'-1'"))


class TblMc(Base):
    __tablename__ = 'tbl_mc'

    uid = Column(Integer, primary_key=True)
    f_order_uid = Column(Integer, index=True, server_default=text("'-1'"))
    f_run_id = Column(String(100), index=True)
    n_samples = Column(Integer)
    f_completion_date = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    f_download = Column(Text)
    f_summary = Column(Text)
    f_my_comment = Column(Text)
    f_admin_comment = Column(Text)
    user_uid = Column(Integer)
    share_user_uid = Column(String(500))


class TblRnaseq(Base):
    __tablename__ = 'tbl_rnaseq'
    __table_args__ = (
        Index('f_order_uid_f_sample_id', 'f_order_uid', 'f_sample_id', unique=True),
    )

    uid = Column(Integer, primary_key=True)
    f_order_uid = Column(Integer, index=True, server_default=text("'-1'"))
    f_sample_id = Column(String(50), index=True, server_default=text("''"))
    f_completion_date = Column(DateTime, index=True, server_default=text("CURRENT_TIMESTAMP"))
    f_sample_name = Column(String(50), server_default=text("''"))
    f_reference_id = Column(String(50), server_default=text("''"))
    f_reference_name = Column(String(200), server_default=text("''"))
    f_download = Column(Text)
    f_download_old = Column(Text)
    f_my_comment = Column(Text)
    f_analysis_name = Column(String(256))
    f_admin_comment = Column(Text)
    user_group_uid = Column(Integer, server_default=text("'-1'"))
    user_uid = Column(Integer, server_default=text("'-1'"))
    share_user_uid = Column(String(500), server_default=text("'-1'"))


class Transcriptome(Base):
    __tablename__ = 'transcriptome'

    uid = Column(Integer, primary_key=True)
    stamp_update = Column(DateTime, nullable=False, server_default=text("'2000-01-01 00:00:00'"))
    stamp_insert = Column(DateTime, nullable=False, server_default=text("'2000-01-01 00:00:00'"))
    comment_user = Column(String)
    comment_internal = Column(String)
    user_group_uid = Column(Integer, nullable=False, server_default=text("'-1'"))
    share_with_lab = Column(Integer, nullable=False, server_default=text("'0'"))
    species = Column(String(250), nullable=False)
    prefix = Column(String(20), nullable=False)
    strain = Column(Text)
    run_uid = Column(Integer, nullable=False, server_default=text("'-1'"))
    method = Column(Integer, nullable=False, server_default=text("'0'"))
    assembler = Column(Integer, nullable=False, server_default=text("'1'"))
    genome_size = Column(Integer, nullable=False, server_default=text("'-1'"))
    gc_ratio = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    read_n = Column(Integer, nullable=False, server_default=text("'-1'"))
    read_total = Column(Integer, nullable=False, server_default=text("'-1'"))
    coverage = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    N75 = Column(Integer, nullable=False, server_default=text("'-1'"))
    N50 = Column(Integer, nullable=False, server_default=text("'-1'"))
    N25 = Column(Integer, nullable=False, server_default=text("'-1'"))
    contig_n = Column(Integer, nullable=False, server_default=text("'-1'"))
    contig_stat = Column(String)
    scaffold_n = Column(Integer, server_default=text("'-1'"))
    ssu_rrn = Column(Text)
    ssu_rrn_acc = Column(Text)
    ssu_rrn_sim = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ssu_rrn_tax = Column(Text)
    ref_ncbi_gpid = Column(Integer)
    ref_ncbi_name = Column(String(250))
    share_user_group = Column(String)


class UserDiscarded(Base):
    __tablename__ = 'user_discarded'

    uid = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    email2 = Column(String(250))
    password = Column(String(250), nullable=False)
    country = Column(String(250))
    iplogin = Column(Integer, server_default=text("'0'"))
    notify = Column(Integer, server_default=text("'1'"))
    user_level = Column(Integer, server_default=text("'0'"))
    user_group = Column(Integer, server_default=text("'-1'"))
    name = Column(String(250), nullable=False)
    name2 = Column(String(250))
    affiliation = Column(String(250))
    tel_office = Column(String(200))
    tel_cell = Column(String(200))
    fax = Column(String(200))
    address = Column(Text)
    comment = Column(Text)
    stamp_update = Column(DateTime, nullable=False, server_default=text("'2001-01-01 00:00:00'"))
    stamp_insert = Column(DateTime, nullable=False, server_default=text("'2001-01-01 00:00:00'"))
    isAdmin = Column(String(1), server_default=text("'N'"))


class UserGroup(Base):
    __tablename__ = 'user_group'

    uid = Column(Integer, primary_key=True)
    name = Column(String(255))
    leader_uid = Column(Integer, nullable=False)
    email = Column(String(255), nullable=False)
    affiliation = Column(Text, nullable=False)
    stamp_update = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    stamp_insert = Column(DateTime, nullable=False, server_default=text("'2001-01-01 00:00:00'"))
    comment_user = Column(String)
    comment_internal = Column(String)
    product_key = Column(String(50))
    auth_key = Column(String(50))


class UserGroupDiscarded(Base):
    __tablename__ = 'user_group_discarded'

    uid = Column(Integer, primary_key=True)
    name = Column(String(255))
    leader_uid = Column(Integer, nullable=False)
    email = Column(String(255), nullable=False)
    affiliation = Column(Text, nullable=False)
    stamp_update = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    stamp_insert = Column(DateTime, nullable=False, server_default=text("'2001-01-01 00:00:00'"))
    comment_user = Column(String)
    comment_internal = Column(String)
    product_key = Column(String(50))
    auth_key = Column(String(50))


t_worker = Table(
    'worker', metadata,
    Column('hostname', String(10)),
    Column('max_proc', Integer),
    Column('defunct', Integer, server_default=text("'0'"))
)
