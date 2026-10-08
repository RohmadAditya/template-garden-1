/**
 * NusaGarden Landscape - Interactive Garden Cost Calculator
 * Allows prospective clients to estimate project budget based on garden style, area, and addons
 */

document.addEventListener('DOMContentLoaded', () => {
  const calcContainer = document.querySelector('.calculator-wrapper');
  if (!calcContainer) return;

  const areaSlider = document.getElementById('calcAreaSlider');
  const areaValueDisplay = document.getElementById('calcAreaValue');
  const typeRadios = document.querySelectorAll('input[name="gardenType"]');
  const addonCheckboxes = document.querySelectorAll('input[name="gardenAddon"]');

  // Result displays
  const resTypeEl = document.getElementById('resGardenType');
  const resAreaEl = document.getElementById('resArea');
  const resBaseCostEl = document.getElementById('resBaseCost');
  const resAddonsEl = document.getElementById('resAddonsCost');
  const resTotalEl = document.getElementById('resTotalCost');
  const btnSendWa = document.getElementById('btnCalcSendWa');

  const ratesPerM2 = {
    'minimalis': { name: 'Taman Minimalis Modern', rate: 350000 },
    'kering': { name: 'Taman Kering (Japanese Zen)', rate: 450000 },
    'tropis': { name: 'Taman Tropis Asri (Bali Style)', rate: 550000 },
    'vertical': { name: 'Vertical Garden (Living Wall)', rate: 1200000 },
    'kolam': { name: 'Kolam Koi & Water Feature', rate: 2200000 }
  };

  const addonPrices = {
    'lighting': { name: 'Lighting & Lampu Sorot Spot', price: 850000 },
    'irrigation': { name: 'Sistem Sprinkler Otomatis', price: 1600000 },
    'stepping': { name: 'Batu Pijakan (Stepping Stone)', price: 650000 },
    'relief': { name: 'Relief Tebing & Mini Fountain', price: 2800000 }
  };

  function formatRupiah(number) {
    return new Intl.NumberFormat('id-ID', {
      style: 'currency',
      currency: 'IDR',
      maximumFractionDigits: 0
    }).format(number);
  }

  function calculate() {
    // 1. Get Area
    const area = parseInt(areaSlider ? areaSlider.value : 20, 10);
    if (areaValueDisplay) {
      areaValueDisplay.textContent = `${area} m²`;
    }

    // 2. Get Selected Type
    let selectedTypeKey = 'minimalis';
    typeRadios.forEach(radio => {
      if (radio.checked) {
        selectedTypeKey = radio.value;
      }
    });

    const typeConfig = ratesPerM2[selectedTypeKey] || ratesPerM2['minimalis'];
    const baseCost = area * typeConfig.rate;

    // 3. Get Selected Addons
    let addonsCost = 0;
    const selectedAddonNames = [];
    addonCheckboxes.forEach(cb => {
      if (cb.checked && addonPrices[cb.value]) {
        addonsCost += addonPrices[cb.value].price;
        selectedAddonNames.push(addonPrices[cb.value].name);
      }
    });

    const totalCost = baseCost + addonsCost;

    // 4. Update UI
    if (resTypeEl) resTypeEl.textContent = typeConfig.name;
    if (resAreaEl) resAreaEl.textContent = `${area} m²`;
    if (resBaseCostEl) resBaseCostEl.textContent = formatRupiah(baseCost);
    if (resAddonsEl) resAddonsEl.textContent = formatRupiah(addonsCost);
    if (resTotalEl) resTotalEl.textContent = formatRupiah(totalCost);

    // 5. Update WhatsApp link
    if (btnSendWa) {
      let addonListText = selectedAddonNames.length > 0 
        ? selectedAddonNames.map(a => `   - ${a}`).join('\n')
        : '   - Tidak ada';

      const waText = `Halo NusaGarden Landscape, saya baru saja mencoba Kalkulator Estimasi Taman di website:\n\n` +
        `• *Tipe Taman:* ${typeConfig.name}\n` +
        `• *Perkiraan Luas Area:* ${area} m²\n` +
        `• *Opsi Tambahan:*\n${addonListText}\n` +
        `• *Estimasi Total Biaya:* ${formatRupiah(totalCost)}\n\n` +
        `Saya tertarik ingin berkonsultasi lebih lanjut dan jadwal survey lokasi. Apakah bisa dibantu?`;

      const encoded = encodeURIComponent(waText);
      btnSendWa.href = `https://wa.me/6281234567890?text=${encoded}`;
    }
  }

  // Event Listeners
  if (areaSlider) {
    areaSlider.addEventListener('input', calculate);
  }
  typeRadios.forEach(radio => radio.addEventListener('change', calculate));
  addonCheckboxes.forEach(cb => cb.addEventListener('change', calculate));

  // Initial Calculation
  calculate();
});

