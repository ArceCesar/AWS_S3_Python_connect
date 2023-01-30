# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 16:44:22 2023
This Script was prepared to auto-transfert (commit) AWS S3 Glue Dev gzipfiles
source: Is a Dictionary 
@author: cearce
"""

# Import Libraries
import sys
import boto3

dev_dictionary = [{'source': 'SAPCO/Inbound/Financials/Costing', 'target': 'SAPCO/Archive/Financials/Costing'}, {'source': 'SAPCO/Inbound/Financials/Profitability', 'target': 'SAPCO/Archive/Financials/Profitability'}, {'source': 'SAPCO/Inbound/Financials/Profitability/Historical', 'target': 'SAPCO/Archive/Financials/Profitability/Historical'}, {'source': 'SAPCO/Inbound/Financials/Profitability/ZIPRFANLZFINLCUB', 'target': 'SAPCO/Archive/Financials/Profitability/ZIPRFANLZFINLCUB'}, {'source': 'SAPCO/Inbound/Inventory/Balances', 'target': 'SAPCO/Archive/Inventory/Balances'}, {'source': 'SAPCO/Inbound/Inventory/Balances/ZISCINVBALFINALC', 'target': 'SAPCO/Archive/Inventory/Balances/ZISCINVBALFINALC'}, {'source': 'SAPCO/Inbound/Inventory/Transactions', 'target': 'SAPCO/Archive/Inventory/Transactions'}, {'source': 'SAPCO/Inbound/Manufacturing/Overview', 'target': 'SAPCO/Archive/Manufacturing/Overview'}, {'source': 'SAPCO/Inbound/Manufacturing/Process Quality', 'target': 'SAPCO/Archive/Manufacturing/Process Quality'}, {'source': 'SAPCO/Inbound/Procurement and Spend/Invoice Lines', 'target': 'SAPCO/Archive/Procurement and Spend/Invoice Lines'}, {'source': 'SAPCO/Inbound/Procurement and Spend/Purchase Orders', 'target': 'SAPCO/Archive/Procurement and Spend/Purchase Orders'}, {'source': 'SAPCO/Inbound/Procurement and Spend/Purchase Receipts', 'target': 'SAPCO/Archive/Procurement and Spend/Purchase Receipts'}, {'source': 'SAPCO/Inbound/Sales/Invoice Lines', 'target': 'SAPCO/Archive/Sales/Invoice Lines'}, {'source': 'SAPCO/Inbound/Sales/Order Lines', 'target': 'SAPCO/Archive/Sales/Order Lines'}, {'source': 'SAPCO/Inbound/Sales/Ship Lines', 'target': 'SAPCO/Archive/Sales/Ship Lines'}, {'source': 'SAPCO/Inbound/Sales/test_TOBEDELETED', 'target': 'SAPCO/Archive/Sales/test_TOBEDELETED'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/FIN/FIN_T001', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/FIN/FIN_T001'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/FIN/T001', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/FIN/T001'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/A526', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/A526'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/A528', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/A528'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/A531', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/A531'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/A532', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/A532'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/A533', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/A533'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/A534', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/A534'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/A537', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/A537'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/A541', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/A541'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/A542', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/A542'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/A701', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/A701'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/A702', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/A702'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/A703', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/A703'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/ADR2', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/ADR2'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/ADR6', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/ADR6'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/ADRC', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/ADRC'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/AUSP', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/AUSP'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/B501', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/B501'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/B503', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/B503'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/B504', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/B504'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/B511', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/B511'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/B512', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/B512'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/BUT000', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/BUT000'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/BUT020', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/BUT020'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/BUT100', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/BUT100'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/DFKKBPTAXNUM', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/DFKKBPTAXNUM'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/EDIPHONE', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/EDIPHONE'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/EDP12', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/EDP12'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/EDP13', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/EDP13'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/EDP21', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/EDP21'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/EDPAR', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/EDPAR'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/EDPP1', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/EDPP1'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/EDSDC', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/EDSDC'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/KNA1', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/KNA1'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/KNB1', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/KNB1'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/KNB5', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/KNB5'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/KNMT', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/KNMT'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/KNMTA', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/KNMTA'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/KNVH', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/KNVH'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/KNVI', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/KNVI'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/KNVP', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/KNVP'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/KNVV', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/KNVV'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/KONDH', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/KONDH'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/KONH', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/KONH'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/KONM', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/KONM'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/KONP', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/KONP'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/KOTH001', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/KOTH001'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/KOTH900', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/KOTH900'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/KOTH903', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/KOTH903'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/NACH', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/NACH'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/STXH', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/STXH'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/STXL', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/STXL'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/TVKO', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/TVKO'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/UDMBPPROFILE', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/UDMBPPROFILE'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/UDMBPSEGMENTS', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/UDMBPSEGMENTS'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/UKMBP', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/UKMBP'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/OTC/ZTCO', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/OTC/ZTCO'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/AFPO', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/AFPO'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/AUFK', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/AUFK'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/CABN', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/CABN'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/CAUFV', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/CAUFV'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/CRCA', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/CRCA'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/CRCO', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/CRCO'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/CRHD', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/CRHD'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/CRTX', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/CRTX'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/KAKO', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/KAKO'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/KAKT', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/KAKT'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/KLAH', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/KLAH'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/MAKT', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/MAKT'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/MAPL', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/MAPL'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/MARA', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/MARA'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/MARC', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/MARC'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/MARD', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/MARD'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/MARM', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/MARM'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/MAST', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/MAST'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/MKAL', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/MKAL'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/MLAN', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/MLAN'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/MVKE', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/MVKE'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/PLKO', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/PLKO'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/PLMK', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/PLMK'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/PLPO', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/PLPO'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/QCVK', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/QCVK'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/QCVM', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/QCVM'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/QCVMT', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/QCVMT'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/QCVV', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/QCVV'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/QMAT', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/QMAT'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/QMTB', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/QMTB'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/QMTT', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/QMTT'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/QPMK', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/QPMK'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/QPMZ', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/QPMZ'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/RESB', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/RESB'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/SAPAPO', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/SAPAPO'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/STKO', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/STKO'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/STPO', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/STPO'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTM/TCRCOT', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTM/TCRCOT'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTP/A017', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTP/A017'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTP/A018', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTP/A018'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTP/EINA', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTP/EINA'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTP/EINE', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTP/EINE'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTP/EORD', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTP/EORD'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTP/KNBK', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTP/KNBK'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTP/LFA1', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTP/LFA1'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTP/LFB1', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTP/LFB1'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTP/LFBK', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTP/LFBK'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTP/LFBW', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTP/LFBW'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTP/LFM1', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTP/LFM1'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTP/T001W', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTP/T001W'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTP/T024E', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTP/T024E'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/PTP/WYT3', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/PTP/WYT3'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/ANEP', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/ANEP'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/ANLA', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/ANLA'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/ANLB', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/ANLB'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/ANLC', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/ANLC'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/ANLH', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/ANLH'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/ANLZ', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/ANLZ'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/BKPF', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/BKPF'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/BNKA', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/BNKA'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/BSET', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/BSET'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/BSIS', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/BSIS'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/CSKS', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/CSKS'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/CSKT', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/CSKT'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/PRHI', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/PRHI'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/PROJ', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/PROJ'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/PRPS', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/PRPS'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/SKA1', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/SKA1'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/SKAT', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/SKAT'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/SKB1', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/SKB1'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/ZBSEG', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/ZBSEG'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/RTR/ZBSIK', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/RTR/ZBSIK'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/AQUA', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/AQUA'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/BINMAT', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/BINMAT'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/CONDINDX', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/CONDINDX'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/HUHDR', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/HUHDR'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/LAGP', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/LAGP'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/MATLWH', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/MATLWH'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/MATLWHST', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/MATLWHST'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/MCHA', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/MCHA'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/MKPF', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/MKPF'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/MSEG', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/MSEG'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/PAPAK', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/PAPAK'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/PNPAKH', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/PNPAKH'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/PVPAKC', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/PVPAKC'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/PVPAKL', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/PVPAKL'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/QUAN', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/QUAN'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SAPAPO/SAPAPO_MATLWH', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SAPAPO/SAPAPO_MATLWH'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SAPAPO/SAPAPO_MATLWHST', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SAPAPO/SAPAPO_MATLWHST'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SAPAPO/SAPAPO_TR', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SAPAPO/SAPAPO_TR'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SAPAPO/SAPAPO_TRM', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SAPAPO/SAPAPO_TRM'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SAPAPO/SAPAPO_TRMC', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SAPAPO/SAPAPO_TRMC'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SAPAPO/SAPAPO_TRMCARR', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SAPAPO/SAPAPO_TRMCARR'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SAPCND', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SAPCND'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SCMB/SCMB_TOENTITY', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SCMB/SCMB_TOENTITY'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SCMB/SCMB_ZONE_D', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SCMB/SCMB_ZONE_D'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SCMB/SCMB_ZONE_P', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SCMB/SCMB_ZONE_P'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SCMB/SCMB_ZONE_R', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SCMB/SCMB_ZONE_R'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SCMB/SCMB_ZONE', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SCMB/SCMB_ZONE'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SCWM/SCWM_AQUA', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SCWM/SCWM_AQUA'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SCWM/SCWM_BINMAT', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SCWM/SCWM_BINMAT'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SCWM/SCWM_HUHDR', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SCWM/SCWM_HUHDR'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SCWM/SCWM_LAGP', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SCWM/SCWM_LAGP'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SCWM/SCWM_PAPAK', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SCWM/SCWM_PAPAK'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SCWM/SCWM_PNPAKH', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SCWM/SCWM_PNPAKH'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SCWM/SCWM_PVPAKC', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SCWM/SCWM_PVPAKC'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SCWM/SCWM_PVPAKL', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SCWM/SCWM_PVPAKL'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/SCWM/SCWM_QUAN', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/SCWM/SCWM_QUAN'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/T001L', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/T001L'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/TR', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/TR'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/TRM', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/TRM'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/TRMC', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/TRMC'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/TRMCARR', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/TRMCARR'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/SC/TVST', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/SC/TVST'}, {'source': 'SAPCO/Inbound/MASTER_DATA_TABLES/TEST/T001', 'target': 'SAPCO/Archive/MASTER_DATA_TABLES/TEST/T001'}]

bucketname = "agropur-global-nonprod-account-dev-sapco"
s3 = boto3.resource('s3')
my_bucket = s3.Bucket(bucketname)

for row in dev_dictionary:
    source=row['source']
    target=row['target']
    result ='source="{}" target="{}"'.format(source, target)
    for obj in my_bucket.object.filter(Prefix=source):
        source_filename = (obj.key).split("/")[-1]
        copy_source = {
            'Bucket':bucketname,
            'Key':obj.key
        }
        target_filename = "{}/{}".format(target, source_filename)
        s3.meta.client.copy(copy_source, bucketname, target_filename)
        # Unconnect the line below if you wish the delete the original source file
        # s3.Object(bucketname, obj.key).delete()