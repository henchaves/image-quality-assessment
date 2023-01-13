import os
import json

def find_duplicates(encoder, group_id, images_dir_path, results_dir_path, threshold=0.85):
    images_group_dir_path = os.path.join(images_dir_path, group_id)
    results_file_name = group_id + ".json"
    results_file_path = os.path.join(results_dir_path, results_file_name)
    duplicates = encoder.find_duplicates(
        image_dir=images_group_dir_path,
        min_similarity_threshold=threshold,
        scores=True,
        outfile=results_file_path
    )