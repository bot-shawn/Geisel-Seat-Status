import React from 'react';
import { View, Text, StyleSheet, ScrollView, SafeAreaView, StatusBar } from 'react-native';
import { WebView } from 'react-native-webview';

export default function GeiselApp() {
  // ACTUAL TABLEAU URL 
  const tableauURL = "https://public.tableau.com/views/geisellibraryheatmap/8thfloor?:embed=yes&:showVizHome=no&:toolbar=no&:device=mobile";

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
            <Text style={styles.headerSubtitle}>Live Check-in Prototype</Text>
          </View>

          <View style={styles.availabilityBox}>
            <Text style={styles.totalAvailableLabel}>TOTAL AVAILABLE</Text>
            <View style={styles.numberRow}>
              <Text style={styles.totalCountGold}>750</Text>
              <Text style={styles.totalDenominator}>/3000</Text>
            </View>
          </View>
        </View>
      </View>

      <ScrollView style={styles.body}>
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>Select a Floor</Text>
          <Text style={styles.zoneCount}>8 Zones</Text>
        </View>

        {/* TABLEAU MAP EMBED */}
        <View style={styles.mapContainer}>
          <WebView 
            source={{ uri: tableauURL }} 
            style={styles.webview}
            scrollEnabled={false}
          />
        </View>

        {/* FLOOR LIST SECTION */}
        <FloorItem name="1st Floor East" type="Collaborative" left={25} percent="83%" color="#E17100" tagStyle={styles.tagCollaborative} />
        <FloorItem name="1st Floor West" type="Collaborative" left={110} percent="79%" color="#E17100" tagStyle={styles.tagCollaborative} />
        <FloorItem name="2nd Floor" type="Collaborative" left={195} percent="85%" color="#E17100" tagStyle={styles.tagCollaborative} />
        <FloorItem name="4th Floor" type="Quiet" left={5} percent="94%" color="#E7000B" tagStyle={styles.tagQuiet} />
        <FloorItem name="5th Floor" type="Quiet" left={55} percent="65%" color="#009966" tagStyle={styles.tagQuiet} />
        <FloorItem name="6th Floor" type="Quiet" left={290} percent="34%" color="#009966" tagStyle={styles.tagQuiet} />
        <FloorItem name="8th Floor" type="Silent" left={5} percent="97%" color="#E7000B" tagStyle={styles.tagSilent} />
      </ScrollView>
    </SafeAreaView>
  );
}

// Reusable Floor Component
interface FloorProps {
  name: string;
  type: string;
  left: number;
  percent: string;
  color: string;
  tagStyle: any; // Using any for the style object to keep it simple
}

function FloorItem({ name, type, left, percent, color, tagStyle }: FloorProps) {
  return (
    <View style={styles.card}>
      <View style={styles.leftBadge}>
        <Text style={styles.leftLabel}>Left</Text>
        <Text style={[styles.leftCount, { color: color }]}>{left}</Text>
      </View>
      <View style={styles.cardInfo}>
        <View style={styles.cardTitleRow}>
          <Text style={styles.floorName}>{name}</Text>
          <View style={[styles.tagContainer, { backgroundColor: type === 'Collaborative' ? '#DBEAFE' : type === 'Quiet' ? '#FEF3C6' : '#F3E8FF' }]}>
             <Text style={[styles.tagText, tagStyle]}>{type}</Text>
          </View>
        </View>
        <View style={styles.progressBg}>
          <View style={[styles.progressFill, { width: percent as any, backgroundColor: color }]} />
        </View>
        <Text style={styles.percentageText}>{percent}</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  // LAYOUT CONTAINERS
  container: { flex: 1, backgroundColor: '#F9FAFB' },
  header: { backgroundColor: '#182B49', paddingVertical: 20, paddingHorizontal: 16 },
  headerContent: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'flex-end', marginTop: 10 },
  logoRow: { flexDirection: 'row', alignItems: 'center' },
  logoIndicator: { width: 4, height: 20, backgroundColor: '#FFCD00', marginRight: 8 },
  availabilityBox: { alignItems: 'flex-end' },
  numberRow: { flexDirection: 'row', alignItems: 'baseline' },
  body: { padding: 16 },
  sectionHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 },
  mapContainer: { height: 400, backgroundColor: '#fff', borderRadius: 14, overflow: 'hidden', marginBottom: 20, borderWidth: 1, borderColor: '#E5E7EB' },
  webview: { flex: 1 },
  
  // CARD STYLES
  card: { flexDirection: 'row', backgroundColor: 'white', padding: 16, borderRadius: 14, marginBottom: 12, borderWidth: 1, borderColor: '#E5E7EB', alignItems: 'center' },
  leftBadge: { width: 52, height: 52, backgroundColor: '#F9FAFB', borderRadius: 10, justifyContent: 'center', alignItems: 'center', marginRight: 12, borderWidth: 1, borderColor: '#F3F4F6' },
  cardInfo: { flex: 1 },
  cardTitleRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 },
  tagContainer: { paddingHorizontal: 8, paddingVertical: 2, borderRadius: 12 },
  progressBg: { height: 8, backgroundColor: '#F3F4F6', borderRadius: 4, overflow: 'hidden' },
  progressFill: { height: 8, borderRadius: 4 },

  // TEXT STYLES (FROM FIGMA)
  headerTitle: { color: 'white', fontSize: 24, fontWeight: '700', lineHeight: 32 },
  headerSubtitle: { color: '#BEDBFF', fontSize: 14, fontWeight: '400', lineHeight: 20 },
  totalAvailableLabel: { color: 'white', fontSize: 10, fontWeight: '600', textTransform: 'uppercase', letterSpacing: 0.6 },
  totalCountGold: { color: '#FFCD00', fontSize: 30, fontWeight: '700', lineHeight: 36 },
  totalDenominator: { color: '#BEDBFF', fontSize: 16, fontWeight: '500' },
  sectionTitle: { color: '#1E2939', fontSize: 18, fontWeight: '700' },
  zoneCount: { color: '#6A7282', fontSize: 14, fontWeight: '500' },
  floorName: { color: '#101828', fontSize: 18, fontWeight: '700' },
  leftLabel: { color: '#6A7282', fontSize: 11, fontWeight: '600' },
  leftCount: { fontSize: 15, fontWeight: '700' },
  percentageText: { color: '#99A1AF', fontSize: 11, fontWeight: '500', textAlign: 'right', marginTop: 4 },
  tagText: { fontSize: 10, fontWeight: '700', textTransform: 'uppercase' },

  // TAG COLORS
  tagCollaborative: { color: '#1447E6' },
  tagQuiet: { color: '#BB4D00' },
  tagSilent: { color: '#8200DB' },
});