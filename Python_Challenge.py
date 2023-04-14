def calculate_class_allocation(num_students):
    max_class_size = 30
    # if the number of students is fewer than 30, we can split them into 2 classes
    if num_students <= max_class_size:
        return {"Class 1": num_students // 2 + num_students % 2, "Class 2": num_students // 2}

    num_classes = (num_students + max_class_size - 1) // max_class_size
    students_evenly_distributed = num_students // num_classes  # students if we just split them equally
    extra_students = num_students % num_classes  # remainder of evenly distributed students

    class_allocation = {}
    for i in range(num_classes):
        additional_student = 0
        if extra_students > 0:
            additional_student = 1
            extra_students -= 1

        students_in_class = students_evenly_distributed + additional_student
        class_allocation[f"Class {i + 1}"] = students_in_class

    print(f"Proposed Allocation: {len(class_allocation)} classes")
    print(f"{class_allocation}")
    return class_allocation

# calling the examples given
calculate_class_allocation(31)
calculate_class_allocation(59)
calculate_class_allocation(87)