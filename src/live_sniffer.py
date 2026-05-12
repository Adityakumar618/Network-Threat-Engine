# --- 2. Feature Extraction & Mapping ---
def extract_and_predict(packet):
    """
    Extracts features from the raw packet, maps them to the CIC-IDS2017 format,
    and runs the anomaly detection inference.
    """
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        packet_len = len(packet)
        
        dst_port = 0
        fin_flag = 0
        syn_flag = 0
        
        # Determine Port and TCP Flags
        if TCP in packet:
            dst_port = packet[TCP].dport
            flags = packet[TCP].flags
            
            # Scapy uses letter codes for flags (F=FIN, S=SYN)
            if 'F' in flags:
                fin_flag = 1
            if 'S' in flags:
                syn_flag = 1
                
        elif UDP in packet:
            dst_port = packet[UDP].dport
            
        # 1. Map to the EXACT 4 features your model was trained on
        model_input = pd.DataFrame([{
            'Destination Port': dst_port,
            'Total Length of Fwd Packets': packet_len,
            'FIN Flag Count': fin_flag,
            'SYN Flag Count': syn_flag
        }])
        
        # 2. ML Inference Pipeline (Bypass strict scikit-learn validation)
        scaled_input = scaler.transform(model_input.values)
        
        # Calculate anomaly score (Higher is more anomalous)
        score = (model.decision_function(scaled_input) * -1)[0]
        
        is_anomaly = score > threshold
        
        # 3. Terminal Output Routing & CSV Logging
        current_time = time.strftime("%H:%M:%S")
        score_str = f"{score:.3f}"
        status = "ALERT" if is_anomaly else "OK"
        
        if is_anomaly:
            # Print anomalies in Red (ANSI Escape Code \033[91m)
            print(f"\033[91m[{current_time}] | {src_ip:<15} | {dst_ip:<15} | {dst_port:<5} | {score_str:<7} | 🚨 ALERT\033[0m")
        else:
            # Print normal traffic in Green (ANSI Escape Code \033[92m)
            print(f"\033[92m[{current_time}] | {src_ip:<15} | {dst_ip:<15} | {dst_port:<5} | {score_str:<7} | OK\033[0m")

        # --- Write to CSV for the Dashboard ---
        with open(csv_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([current_time, src_ip, dst_ip, dst_port, score_str, status])