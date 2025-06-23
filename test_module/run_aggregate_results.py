import argparse
from test_module.config import Config
# from ptm_search.postprocessing.aggregate_results import aggregate_ptm_results

def main():
    parser = argparse.ArgumentParser(description="Aggregate PTM search results")
    parser.add_argument('--config', type=str, default='pipeline.cfg', help='Path to config file')
    args = parser.parse_args()

    config = Config(args.config)
    print('Run aggregate result')
    print(config.experiment_name)
    print(config.analysis_index)
    print(config.base_path)
    print(config.fasta_path)
    print(config.base_config_path)
    # aggregate_ptm_results(config)
