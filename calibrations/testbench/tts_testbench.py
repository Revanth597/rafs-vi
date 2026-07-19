from maix import camera, pinmap, display, touchscreen, image, nn, app, time, gpio
import math

# ============================================================
# IEEE CS PAPER TEST VERSION
# ============================================================

# ------------------------------------------------------------
# TEST SETTINGS
# ------------------------------------------------------------
TEST_DISTANCES = [0.5,1]

TEST_OBJECTS = ["person"]

SAMPLES_PER_TEST = 20
OBJECT_CHANGE_DELAY = 15  # seconds

# ------------------------------------------------------------
# KNOWN OBJECT WIDTHS (meters)
# ------------------------------------------------------------
object_widths = {
    "chair": 0.50,
    "person": 0.45,
    "suitcase": 0.35,
    "laptop": 0.32,
    "cell phone": 0.08,
    "bottle":0.074,
    "keyboard":0.33,
    "vase":0.6,
    "suitcase":0.68
}

# ------------------------------------------------------------
# CAMERA PARAMETERS
# ------------------------------------------------------------
FOCAL_LENGTH_MM = 4.37
SENSOR_WIDTH_MM = 6.4

# ============================================================
# INITIALIZE YOLO MODEL
# ============================================================

detector = nn.YOLO11(
    model="/root/models/yolo11n.mud",
    dual_buff=True
)

# ============================================================
# CAMERA + DISPLAY
# ============================================================

cam = camera.Camera(
    detector.input_width(),
    detector.input_height(),
    detector.input_format()
)

disp = display.Display()
ts = touchscreen.TouchScreen()

# ============================================================
# BUTTON + LED
# ============================================================

button_pin = gpio.GPIO(
    "A19",
    mode=gpio.Mode.IN,
    pull=gpio.Pull.PULL_UP
)

pinmap.set_pin_function("A18", "GPIOA18")

led = gpio.GPIO(
    "GPIOA18",
    gpio.Mode.OUT
)

led.value(0)

# ============================================================
# VARIABLES
# ============================================================

detection_enabled = False
button_prev_state = 1

sample_count = 0

current_object_index = 0
current_distance_index = 0

testing_done = False

# ============================================================
# RESULTS STORAGE
# ============================================================

results = {}

for obj in TEST_OBJECTS:

    results[obj] = {}

    for d in TEST_DISTANCES:

        results[obj][d] = {
            "estimated_distances": [],
            "bbox_widths": [],
            "bbox_heights": []
        }

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def is_in_button(x, y, btn_pos):

    return (
        x > btn_pos[0]
        and x < btn_pos[0] + btn_pos[2]
        and y > btn_pos[1]
        and y < btn_pos[1] + btn_pos[3]
    )

def mean(values):

    if len(values) == 0:
        return 0

    return sum(values) / len(values)

def stddev(values):

    if len(values) <= 1:
        return 0

    m = mean(values)

    variance = sum((x - m) ** 2 for x in values) / len(values)

    return math.sqrt(variance)

def calculate_distance(known_width, pixel_width):

    distance_m = (
        known_width
        * FOCAL_LENGTH_MM
        * detector.input_width()
    ) / (
        pixel_width
        * SENSOR_WIDTH_MM
    )

    return distance_m

# ============================================================
# START MESSAGE
# ============================================================

print("\n===================================================")
print("IEEE CS PAPER TEST MODE")
print("===================================================")

print("\nObjects:")
for o in TEST_OBJECTS:
    print(" -", o)

print("\nDistances:")
for d in TEST_DISTANCES:
    print(" -", d, "m")

print("\nInstructions:")
print("1. Place object at required distance")
print("2. Press hardware button to START")
print("3. 20 samples collected automatically")
print("4. 15 second setup break")
print("5. Press button again for next measurement")
print("===================================================\n")

# ============================================================
# MAIN LOOP
# ============================================================

while not app.need_exit():

    img = cam.read()

    # --------------------------------------------------------
    # EXIT BUTTON
    # --------------------------------------------------------

    exit_label = "< Exit"

    size = image.string_size(exit_label)

    exit_btn_pos = [
        0,
        0,
        8 * 2 + size.width(),
        12 * 2 + size.height()
    ]

    img.draw_string(
        8,
        12,
        exit_label,
        image.COLOR_WHITE
    )

    img.draw_rect(
        exit_btn_pos[0],
        exit_btn_pos[1],
        exit_btn_pos[2],
        exit_btn_pos[3],
        image.COLOR_WHITE,
        2
    )

    x, y, pressed = ts.read()

    if is_in_button(x, y, exit_btn_pos):
        app.set_exit_flag(True)

    # --------------------------------------------------------
    # BUTTON TOGGLE
    # --------------------------------------------------------

    button_state = button_pin.value()

    if button_prev_state == 1 and button_state == 0:

        detection_enabled = not detection_enabled

        print(
            "\nDetection",
            "ENABLED" if detection_enabled else "DISABLED"
        )

        led.value(1 if detection_enabled else 0)

        time.sleep_ms(300)

    button_prev_state = button_state

    # --------------------------------------------------------
    # DETECTION OFF
    # --------------------------------------------------------

    if not detection_enabled:

        img.draw_string(
            40,
            100,
            "PRESS BUTTON TO START",
            color=image.COLOR_RED,
            scale=1.6
        )

        disp.show(img)
        continue

    # --------------------------------------------------------
    # ALL TESTS COMPLETE
    # --------------------------------------------------------

    if testing_done:

        print("\n===================================================")
        print("FINAL IEEE PAPER RESULTS")
        print("===================================================")

        for obj in TEST_OBJECTS:

            print("\nOBJECT:", obj.upper())

            for dist in TEST_DISTANCES:

                data = results[obj][dist]

                estimated_distances = data["estimated_distances"]
                bbox_widths = data["bbox_widths"]
                bbox_heights = data["bbox_heights"]

                if len(estimated_distances) == 0:
                    continue

                # ------------------------------------------------
                # DISTANCE STATS
                # ------------------------------------------------

                avg_distance = mean(estimated_distances)
                std_distance = stddev(estimated_distances)

                # ------------------------------------------------
                # WIDTH STATS
                # ------------------------------------------------

                avg_bbox_width = mean(bbox_widths)
                std_bbox_width = stddev(bbox_widths)

                min_bbox_width = min(bbox_widths)
                max_bbox_width = max(bbox_widths)

                # ------------------------------------------------
                # HEIGHT STATS
                # ------------------------------------------------

                avg_bbox_height = mean(bbox_heights)
                std_bbox_height = stddev(bbox_heights)

                min_bbox_height = min(bbox_heights)
                max_bbox_height = max(bbox_heights)

                # ------------------------------------------------
                # WIDTH / HEIGHT RATIO
                # ------------------------------------------------

                aspect_ratios = []

                for w, h in zip(bbox_widths, bbox_heights):

                    if h != 0:
                        aspect_ratios.append(w / h)

                avg_aspect_ratio = mean(aspect_ratios)
                std_aspect_ratio = stddev(aspect_ratios)

                min_aspect_ratio = min(aspect_ratios)
                max_aspect_ratio = max(aspect_ratios)

                print("\nDistance {}m".format(dist))

                print(
                    "Distance = {:.3f} ± {:.3f} m".format(
                        avg_distance,
                        std_distance
                    )
                )

                print(
                    "BBox Width = {:.2f} ± {:.2f} px".format(
                        avg_bbox_width,
                        std_bbox_width
                    )
                )

                print(
                    "BBox Height = {:.2f} ± {:.2f} px".format(
                        avg_bbox_height,
                        std_bbox_height
                    )
                )

                print(
                    "Width Range = [{:.2f} : {:.2f}] px".format(
                        min_bbox_width,
                        max_bbox_width
                    )
                )

                print(
                    "Height Range = [{:.2f} : {:.2f}] px".format(
                        min_bbox_height,
                        max_bbox_height
                    )
                )

                print(
                    "Width/Height Ratio = {:.3f} ± {:.3f}".format(
                        avg_aspect_ratio,
                        std_aspect_ratio
                    )
                )

                print(
                    "Ratio Range = [{:.3f} : {:.3f}]".format(
                        min_aspect_ratio,
                        max_aspect_ratio
                    )
                )

        print("\n===================================================")

        while True:

            img = cam.read()

            img.draw_string(
                40,
                120,
                "ALL TESTS COMPLETE",
                color=image.COLOR_GREEN,
                scale=2
            )

            disp.show(img)

    # ========================================================
    # CURRENT TEST INFO
    # ========================================================

    current_object = TEST_OBJECTS[current_object_index]

    ground_truth_distance = TEST_DISTANCES[current_distance_index]

    status_text = (
        "{} @ {}m".format(
            current_object,
            ground_truth_distance
        )
    )

    img.draw_string(
        20,
        20,
        status_text,
        color=image.COLOR_GREEN,
        scale=1.5
    )

    # ========================================================
    # YOLO DETECTION
    # ========================================================

    objs = detector.detect(
        img,
        conf_th=0.8,
        iou_th=0.75
    )

    detected = False

    if objs:

        for obj in objs:

            label = detector.labels[obj.class_id]

            label_norm = label.lower()

            if label_norm == "cellphone":
                label_norm = "cell phone"

            # ------------------------------------------------
            # ONLY TARGET OBJECT
            # ------------------------------------------------

            if label_norm != current_object:
                continue

            detected = True

            # ------------------------------------------------
            # DRAW BOX
            # ------------------------------------------------

            img.draw_rect(
                obj.x,
                obj.y,
                obj.w,
                obj.h,
                color=image.COLOR_RED
            )

            bbox_width = obj.w
            bbox_height = obj.h

            # ------------------------------------------------
            # DISTANCE ESTIMATION
            # ------------------------------------------------

            known_width = object_widths[current_object]

            estimated_distance = calculate_distance(
                known_width,
                bbox_width
            )

            # ------------------------------------------------
            # STORE DATA
            # ------------------------------------------------

            results[current_object][ground_truth_distance]["estimated_distances"].append(
                estimated_distance
            )

            results[current_object][ground_truth_distance]["bbox_widths"].append(
                bbox_width
            )

            results[current_object][ground_truth_distance]["bbox_heights"].append(
                bbox_height
            )

            sample_count += 1

            # ------------------------------------------------
            # PRINT SAMPLE INFO
            # ------------------------------------------------

            print("\n--------------------------------------")
            print("OBJECT:", current_object)
            print("GROUND TRUTH:", ground_truth_distance, "m")

            print(
                "ESTIMATED DISTANCE:",
                round(estimated_distance, 3),
                "m"
            )

            print(
                "BOUNDING BOX WIDTH:",
                bbox_width,
                "pixels"
            )

            print(
                "BOUNDING BOX HEIGHT:",
                bbox_height,
                "pixels"
            )

            print(
                "SAMPLE:",
                sample_count,
                "/",
                SAMPLES_PER_TEST
            )

            # ------------------------------------------------
            # DRAW TEXT
            # ------------------------------------------------

            msg = (
                "{} {:.2f}m".format(
                    current_object,
                    estimated_distance
                )
            )

            img.draw_string(
                obj.x,
                obj.y - 20,
                msg,
                color=image.COLOR_YELLOW
            )

            # ------------------------------------------------
            # TEST COMPLETE?
            # ------------------------------------------------

            if sample_count >= SAMPLES_PER_TEST:

                current_data = results[current_object][ground_truth_distance]

                estimated_distances = current_data["estimated_distances"]
                bbox_widths = current_data["bbox_widths"]
                bbox_heights = current_data["bbox_heights"]

                # ------------------------------------------------
                # DISTANCE STATS
                # ------------------------------------------------

                avg_distance = mean(estimated_distances)
                std_distance = stddev(estimated_distances)

                # ------------------------------------------------
                # WIDTH STATS
                # ------------------------------------------------

                avg_bbox_width = mean(bbox_widths)
                std_bbox_width = stddev(bbox_widths)

                min_bbox_width = min(bbox_widths)
                max_bbox_width = max(bbox_widths)

                # ------------------------------------------------
                # HEIGHT STATS
                # ------------------------------------------------

                avg_bbox_height = mean(bbox_heights)
                std_bbox_height = stddev(bbox_heights)

                min_bbox_height = min(bbox_heights)
                max_bbox_height = max(bbox_heights)

                # ------------------------------------------------
                # WIDTH / HEIGHT RATIO
                # ------------------------------------------------

                aspect_ratios = []

                for w, h in zip(bbox_widths, bbox_heights):

                    if h != 0:
                        aspect_ratios.append(w / h)

                avg_aspect_ratio = mean(aspect_ratios)
                std_aspect_ratio = stddev(aspect_ratios)

                min_aspect_ratio = min(aspect_ratios)
                max_aspect_ratio = max(aspect_ratios)

                print("\n======================================")
                print(
                    "RESULT FOR {} @ {}m".format(
                        current_object.upper(),
                        ground_truth_distance
                    )
                )

                print(
                    "DISTANCE = {:.3f} ± {:.3f} m".format(
                        avg_distance,
                        std_distance
                    )
                )

                print(
                    "BOUNDING BOX WIDTH = {:.2f} ± {:.2f} px".format(
                        avg_bbox_width,
                        std_bbox_width
                    )
                )

                print(
                    "BOUNDING BOX HEIGHT = {:.2f} ± {:.2f} px".format(
                        avg_bbox_height,
                        std_bbox_height
                    )
                )

                print(
                    "WIDTH RANGE = [{:.2f} : {:.2f}] px".format(
                        min_bbox_width,
                        max_bbox_width
                    )
                )

                print(
                    "HEIGHT RANGE = [{:.2f} : {:.2f}] px".format(
                        min_bbox_height,
                        max_bbox_height
                    )
                )

                print(
                    "WIDTH / HEIGHT RATIO = {:.3f} ± {:.3f}".format(
                        avg_aspect_ratio,
                        std_aspect_ratio
                    )
                )

                print(
                    "RATIO RANGE = [{:.3f} : {:.3f}]".format(
                        min_aspect_ratio,
                        max_aspect_ratio
                    )
                )

                print("======================================")

                # ------------------------------------------------
                # RESET COUNTER
                # ------------------------------------------------

                sample_count = 0

                # ------------------------------------------------
                # MOVE TO NEXT TEST
                # ------------------------------------------------

                current_distance_index += 1

                if current_distance_index >= len(TEST_DISTANCES):

                    current_distance_index = 0
                    current_object_index += 1

                # ------------------------------------------------
                # FINISHED ALL TESTS?
                # ------------------------------------------------

                if current_object_index >= len(TEST_OBJECTS):

                    testing_done = True

                else:

                    next_object = TEST_OBJECTS[current_object_index]

                    next_distance = TEST_DISTANCES[current_distance_index]

                    print("\n--------------------------------------")
                    print("CHANGE SETUP NOW")

                    print(
                        "NEXT TEST: {} at {}m".format(
                            next_object,
                            next_distance
                        )
                    )

                    print(
                        "Waiting {} seconds before next run...".format(
                            OBJECT_CHANGE_DELAY
                        )
                    )

                    print("After setup, PRESS BUTTON to start next test")
                    print("--------------------------------------\n")

                    # ------------------------------------------------
                    # 15 SECOND BREAK
                    # ------------------------------------------------

                    for i in range(OBJECT_CHANGE_DELAY, 0, -1):

                        img = cam.read()

                        img.draw_string(
                            10,
                            80,
                            "CHANGE OBJECT / DISTANCE",
                            color=image.COLOR_YELLOW,
                            scale=1.3
                        )

                        img.draw_string(
                            40,
                            130,
                            "Next: {} @ {}m".format(
                                next_object,
                                next_distance
                            ),
                            color=image.COLOR_BLUE,
                            scale=1.5
                        )

                        img.draw_string(
                            60,
                            180,
                            "{} sec remaining".format(i),
                            color=image.COLOR_RED,
                            scale=2
                        )

                        disp.show(img)

                        time.sleep(1)

                    # ------------------------------------------------
                    # DISABLE DETECTION
                    # ------------------------------------------------

                    detection_enabled = False

                    led.value(0)

                    print("\n======================================")
                    print("READY FOR NEXT MEASUREMENT")
                    print("PRESS HARDWARE BUTTON TO START")
                    print("======================================\n")

                    # ------------------------------------------------
                    # WAIT FOR USER BUTTON PRESS
                    # ------------------------------------------------

                    while True:

                        img = cam.read()

                        img.draw_string(
                            20,
                            100,
                            "PRESS BUTTON",
                            color=image.COLOR_GREEN,
                            scale=2
                        )

                        img.draw_string(
                            20,
                            150,
                            "TO START NEXT TEST",
                            color=image.COLOR_GREEN,
                            scale=1.5
                        )

                        disp.show(img)

                        button_state = button_pin.value()

                        if button_prev_state == 1 and button_state == 0:

                            detection_enabled = True

                            led.value(1)

                            print("NEXT TEST STARTED\n")

                            time.sleep_ms(300)

                            break

                        button_prev_state = button_state

            break

    # --------------------------------------------------------
    # NO DETECTION
    # --------------------------------------------------------

    if not detected:

        img.draw_string(
            20,
            60,
            "No target detected",
            color=image.COLOR_RED,
            scale=1.5
        )

    disp.show(img)

# ============================================================
# CLEANUP
# ============================================================

cam.close()
disp.close()