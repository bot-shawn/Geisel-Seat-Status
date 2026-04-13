import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ScrollView, SafeAreaView, TouchableOpacity, StatusBar, Alert } from 'react-native';
import { WebView } from 'react-native-webview';

export default function GeiselApp() {
  // 1. STATE - Fixed with proper types to remove red squiggles
  const [seatData, setSeatData] = useState<{
    total: number;
    floors: { [key: string]: number };
  }>({ total: 0, floors: {} });

  const [selectedFloor, setSelectedFloor] = useState<string | null>(null);

  // !!! IMPORTANT: Change this to your Mac's IP Address
  const IP_ADDR = "192.168.1.XX"; 
  const tableauURL = "https://public.tableau.com/views/geisellibraryheatmap/8thfloor?:embed=yes&:showVizHome=no&:toolbar=no&:device=mobile";

  // 2. LIVE DATA SYNC
  useEffect(() => {
    const interval = setInterval(async () => {
      try {
        const response = await fetch(`http://${IP_ADDR}:5000/seats`);
        const data = await response.json();
        setSeatData(data);
      } catch (e) {
        console.log("Searching for Python server...");
      }
    }, 2000);
    return () => clearInterval(interval);
  }, []);

  // 3. CHECK-IN FUNCTION
  const handleCheckIn = async () => {
    if (!selectedFloor) {
      Alert.alert("Wait!", "Please select a floor from the list first.");
      return;
    }
    try {
      const res = await fetch(`http://${IP_ADDR}:5000/checkin`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ floor: selectedFloor }),
      });
      if (res.ok) Alert.alert("Success", `You are checked into ${selectedFloor}`);
    } catch (e) {
      Alert.alert("Offline", "Couldn't connect to the simulator.");
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="light-content" />
      
      {/* HEADER SECTION */}
      <View style={styles.header}>
        <View style={styles.headerContent}>
          <View>
            <View style={styles.logoRow}>
              <View style={styles.logoIndicator} />
              <Text style={styles.headerTitle}>Geisel Seats</Text>
            </View>
            <Text style={styles.headerSubtitle}>Live Prototype</Text>
          </View>
          <View style={styles.availabilityBox}>
            <Text style={styles.totalAvailableLabel}>TOTAL AVAILABLE</Text>
            <View style={styles.numberRow}>
              <Text style={styles.totalCountGold}>{seatData.total}</Text>
              <Text style={styles.totalDenominator}>/3000</Text>
            </View>
          </View>
        </View>
      </View>

      <ScrollView style={styles.body}>
        <Text style={styles.sectionTitle}>Select a Floor</Text>

        {/* MAP EMBED */}
        <View style={styles.mapContainer}>
          <WebView source={{ uri: tableauURL }} style={styles.webview} scrollEnabled={false} />
        </View>

        {/* FULL FLOOR LIST */}
        {[
          { id: "1st Floor (Social)", label: "1st Floor East", type: "Collaborative", pct: "83%", color: "#E17100" },
          { id: "1st Floor (Quiet)", label: "1st Floor West", type: "Quiet", pct: "79%", color: "#E17100" },
          { id: "2nd Floor (Main)", label: "2nd Floor", type: "Collaborative", pct: "85%", color: "#E17100" },
          { id: "4th Floor (Quiet)", label: "4th Floor", type: "Quiet", pct: "94%", color: "#E7000B" },
          { id: "5th Floor (Quiet)", label: "5th Floor", type: "Quiet", pct: "88%", color: "#E7000B" },
          { id: "6th Floor (Quiet)", label: "6th Floor", type: "Quiet", pct: "90%", color: "#E7000B" },
          { id: "7th Floor (Quiet)", label: "7th Floor", type: "Quiet", pct: "92%", color: "#E7000B" },
          { id: "8th Floor (Silent)", label: "8th Floor", type: "Silent", pct: "97%", color: "#E7000B" }
        ].map((f) => (
          <TouchableOpacity 
            key={f.id} 
            onPress={() => setSelectedFloor(f.id)}
            style={[styles.card, selectedFloor === f.id && styles.selectedCard]}
          >
            <View style={styles.leftBadge}>
              <Text style={styles.leftLabel}>Left</Text>
              <Text style={[styles.leftCount, { color: f.color }]}>{seatData.floors[f.id] || 0}</Text>
            </View>
            <View style={styles.cardInfo}>
              <View style={styles.cardTitleRow}>
                <Text style={styles.floorName}>{f.label}</Text>
                <View style={styles.tagContainer}><Text style={styles.tagText}>{f.type}</Text></View>
              </View>
              <View style={styles.progressBg}>
                <View style={[
                  styles.progressFill, 
                  { width: f.pct as any, backgroundColor: f.color } // Added 'as any' here
                ]} />
              </View>
            </View>
          </TouchableOpacity>
        ))}
      </ScrollView>

      {/* CHECK-IN BUTTON */}
      <TouchableOpacity style={styles.checkInBtn} onPress={handleCheckIn}>
        <Text style={styles.checkInText}>
          {selectedFloor ? `Check Into ${selectedFloor.split(' ')[0]} Floor` : "Select a Floor"}
        </Text>
      </TouchableOpacity>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#F9FAFB' },
  header: { backgroundColor: '#182B49', padding: 20 },
  headerContent: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'flex-end' },
  logoRow: { flexDirection: 'row', alignItems: 'center' },
  logoIndicator: { width: 4, height: 20, backgroundColor: '#FFCD00', marginRight: 8 },
  headerTitle: { color: 'white', fontSize: 24, fontWeight: '700' },
  headerSubtitle: { color: '#BEDBFF', fontSize: 12 },
  availabilityBox: { alignItems: 'flex-end' },
  numberRow: { flexDirection: 'row', alignItems: 'baseline' },
  totalCountGold: { color: '#FFCD00', fontSize: 30, fontWeight: '700' },
  totalDenominator: { color: '#BEDBFF', fontSize: 16 },
  totalAvailableLabel: { color: 'white', fontSize: 10, fontWeight: '600' },
  body: { padding: 16 },
  sectionTitle: { fontSize: 18, fontWeight: '700', marginBottom: 16, color: '#1E2939' },
  mapContainer: { height: 300, backgroundColor: '#fff', borderRadius: 14, overflow: 'hidden', marginBottom: 20, borderWidth: 1, borderColor: '#E5E7EB' },
  webview: { flex: 1 },
  card: { flexDirection: 'row', backgroundColor: 'white', padding: 16, borderRadius: 14, marginBottom: 12, borderWidth: 1, borderColor: '#E5E7EB' },
  selectedCard: { borderColor: '#1447E6', backgroundColor: '#F0F7FF', borderWidth: 2 },
  leftBadge: { width: 50, height: 50, backgroundColor: '#F9FAFB', borderRadius: 10, justifyContent: 'center', alignItems: 'center', marginRight: 12 },
  leftLabel: { color: '#6A7282', fontSize: 10, fontWeight: '600' },
  leftCount: { fontSize: 18, fontWeight: '700' },
  cardInfo: { flex: 1, justifyContent: 'center' },
  cardTitleRow: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 8 },
  floorName: { fontSize: 16, fontWeight: '700', color: '#101828' },
  tagContainer: { backgroundColor: '#E5E7EB', paddingHorizontal: 6, borderRadius: 8 },
  tagText: { fontSize: 10, fontWeight: '600', color: '#4B5563' },
  progressBg: { height: 6, backgroundColor: '#F3F4F6', borderRadius: 3 },
  progressFill: { height: 6, borderRadius: 3 },
  checkInBtn: { backgroundColor: '#182B49', margin: 20, padding: 18, borderRadius: 15, alignItems: 'center', elevation: 5 },
  checkInText: { color: 'white', fontWeight: 'bold', fontSize: 18 }
});