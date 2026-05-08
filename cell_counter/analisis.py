import cv2
import numpy as np
def count_cells_by_regions(binary_image, min_area=50, max_area=10000):

    if binary_image.dtype != np.uint8:
        binary_image = (binary_image > 0).astype(np.uint8) * 255

 
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_image, connectivity=8)

    output_img = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)
    
    cell_count = 0
    valid_cells_data = []

    for i in range(1, num_labels): 
        area = stats[i, cv2.CC_STAT_AREA]

        if area >= min_area and area <= max_area:
            cell_count += 1
            
            x = stats[i, cv2.CC_STAT_LEFT]
            y = stats[i, cv2.CC_STAT_TOP]
            w = stats[i, cv2.CC_STAT_WIDTH]
            h = stats[i, cv2.CC_STAT_HEIGHT]
            

            cv2.rectangle(output_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(output_img, str(cell_count), (x, y - 5), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            
            valid_cells_data.append({
                "id": cell_count,
                "centroid": centroids[i],
                "area": area
            })

    return cell_count, output_img, valid_cells_data