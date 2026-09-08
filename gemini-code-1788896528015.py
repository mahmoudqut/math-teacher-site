html_content = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>اختبار تشخيصي في الرياضيات - الصف الحادي عشر العلمي</title>
    <style>
        :root {
            --primary-color: #1a4d2e;
            --secondary-color: #4e9f3d;
            --accent-color: #d8f3dc;
            --text-color: #2b2b2b;
            --bg-color: #f8f9fa;
            --card-bg: #ffffff;
            --border-color: #e0e0e0;
            --correct-bg: #d4edda;
            --correct-border: #c3e6cb;
            --correct-text: #155724;
            --incorrect-bg: #f8d7da;
            --incorrect-border: #f5c6cb;
            --incorrect-text: #721c24;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 20px;
            direction: rtl;
            text-align: right;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            background: var(--card-bg);
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            border: 1px solid var(--border-color);
        }

        /* Header Styling */
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 3px double var(--primary-color);
            padding-bottom: 15px;
            margin-bottom: 25px;
        }

        .header-title {
            text-align: center;
            flex-grow: 1;
        }

        .header-title h1 {
            font-size: 20px;
            color: var(--primary-color);
            margin: 5px 0;
        }

        .header-title h2 {
            font-size: 18px;
            color: #444;
            margin: 5px 0;
            font-weight: normal;
        }

        .header-title h3 {
            font-size: 16px;
            color: var(--secondary-color);
            margin: 5px 0;
        }

        .logo-placeholder {
            width: 80px;
            height: 80px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            color: var(--primary-color);
        }

        /* Student Info Form */
        .student-info {
            background-color: var(--accent-color);
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
            border: 1px solid #c2eabd;
        }

        .form-group {
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
        }

        .form-field {
            flex: 1;
            min-width: 250px;
        }

        .form-field label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
            color: var(--primary-color);
        }

        .form-field input, .form-field select {
            width: 100%;
            padding: 10px;
            border: 1px solid #99c2a2;
            border-radius: 6px;
            font-size: 15px;
            box-sizing: border-box;
            background-color: white;
        }

        .form-field input:focus, .form-field select:focus {
            outline: none;
            border-color: var(--primary-color);
            box-shadow: 0 0 5px rgba(26, 77, 46, 0.3);
        }

        .required-star {
            color: red;
        }

        /* Questions Styling */
        .question-card {
            background: #fff;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            transition: all 0.2s ease;
        }

        .question-card:hover {
            border-color: var(--secondary-color);
        }

        .question-title {
            font-size: 16px;
            font-weight: bold;
            margin-bottom: 15px;
            color: #111;
            line-height: 1.6;
        }

        .options-list {
            list-style-type: none;
            padding: 0;
            margin: 0;
        }

        .option-item {
            margin-bottom: 10px;
        }

        .option-label {
            display: flex;
            align-items: center;
            padding: 10px 15px;
            border: 1px solid #eee;
            border-radius: 6px;
            cursor: pointer;
            transition: background-color 0.2s;
        }

        .option-label:hover {
            background-color: #f0f7f4;
        }

        .option-label input[type="radio"] {
            margin-left: 12px;
            transform: scale(1.2);
            cursor: pointer;
        }

        .math-text {
            font-family: 'Traditional Arabic', 'Amiri', 'Segoe UI', serif;
            font-size: 1.1em;
            font-weight: 600;
        }

        /* Controls */
        .btn-submit {
            display: block;
            width: 100%;
            padding: 14px;
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s;
            margin-top: 30px;
        }

        .btn-submit:hover {
            background-color: #123720;
        }

        /* Result Section */
        #result-section {
            display: none;
            margin-top: 30px;
            padding: 25px;
            background-color: #eef7ee;
            border: 2px solid var(--secondary-color);
            border-radius: 8px;
            text-align: center;
        }

        .score-display {
            font-size: 24px;
            font-weight: bold;
            color: var(--primary-color);
            margin-bottom: 10px;
        }

        /* Correct / Incorrect Feedback Styles */
        .feedback-box {
            margin-top: 10px;
            padding: 10px 15px;
            border-radius: 6px;
            font-size: 14px;
            font-weight: bold;
            display: none;
        }

        .correct-answer-text {
            color: var(--correct-text);
            background-color: var(--correct-bg);
            border: 1px solid var(--correct-border);
        }

        .wrong-answer-text {
            color: var(--incorrect-text);
            background-color: var(--incorrect-bg);
            border: 1px solid var(--incorrect-border);
        }

        .selected-correct {
            background-color: var(--correct-bg) !important;
            border-color: var(--correct-border) !important;
        }

        .selected-wrong {
            background-color: var(--incorrect-bg) !important;
            border-color: var(--incorrect-border) !important;
        }

        .highlight-correct {
            border: 2px solid var(--secondary-color) !important;
            background-color: #e8f5e9 !important;
        }

        .error-message {
            color: red;
            font-size: 14px;
            margin-top: 5px;
            display: none;
        }
    </style>
</head>
<body>

<div class="container">
    <!-- Header -->
    <div class="header">
        <div class="logo-placeholder">
            <svg width="60" height="60" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect width="100" height="100" rx="10" fill="#1a4d2e"/>
                <path d="M20 30H80M20 50H80M20 70H50" stroke="white" stroke-width="8" stroke-linecap="round"/>
            </svg>
        </div>
        <div class="header-title">
            <h1>دولة فلسطين</h1>
            <h2>وزارة التربية والتعليم العالي</h2>
            <h2>مديرية التربية والتعليم - جنوب نابلس</h2>
            <h3>مدرسة مادما الثانوية المختلطة (أ)</h3>
            <h2 style="margin-top:10px; font-weight:bold; color:var(--primary-color);">الاختبار التشخيصي في مبحث الرياضيات</h2>
            <p style="margin: 3px 0; font-size: 14px;"><strong>الصف:</strong> الحادي عشر العلمي | <strong>العام الدراسي:</strong> ٢٠٢٦/٢٠٢٥م</p>
        </div>
        <div class="logo-placeholder">
            <svg width="60" height="60" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="50" cy="50" r="45" stroke="#1a4d2e" stroke-width="5" fill="none"/>
                <path d="M30 50 L45 65 L70 35" stroke="#4e9f3d" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        </div>
    </div>

    <!-- Student Info Form -->
    <form id="quizForm" onsubmit="submitQuiz(event)">
        <div class="student-info">
            <div class="form-group">
                <div class="form-field">
                    <label for="studentName">اسم الطالب/ـة الثلاثي <span class="required-star">*</span></label>
                    <input type="text" id="studentName" required placeholder="أدخل اسمك الكامل هنا">
                    <div class="error-message" id="nameError">يرجى إدخال الاسم قبل بدء الاختبار.</div>
                </div>
                <div class="form-field">
                    <label for="studentClass">الصف والشعبة <span class="required-star">*</span></label>
                    <select id="studentClass" required>
                        <option value="">اختر الشعبة...</option>
                        <option value="الحادي عشر العلمي (أ)">الحادي عشر العلمي (أ)</option>
                        <option value="الحادي عشر العلمي (ب)">الحادي عشر العلمي (ب)</option>
                    </select>
                    <div class="error-message" id="classError">يرجى اختيار الصف والشعبة.</div>
                </div>
            </div>
        </div>

        <p style="background:#f0f4f8; padding:10px 15px; border-right:4px solid var(--primary-color); font-weight:bold; margin-bottom:20px;">
            تعليمات: يتكون هذا الاختبار من (٢٥) فقرة من نوع الاختيار من متعدد. اختر الإجابة الصحيحة لكل فقرة.
        </p>

        <!-- Questions Container -->
        <div id="questions-container"></div>

        <button type="submit" class="btn-submit" id="submitBtn">تسليم الاختبار وحفظ البيانات</button>
    </form>

    <!-- Results Display Section -->
    <div id="result-section">
        <div class="score-display" id="scoreText"></div>
        <p id="feedbackText" style="font-size: 16px; color: #555;"></p>
        <p style="font-size: 13px; color: #777;">تم حفظ بياناتك وإجاباتك بنجاح في النظام المحلي.</p>
    </div>
</div>

<script>
    // 25 Questions based on the image content ( الاقتران الزوجي والفردي, الانسحاب, الانعكاس, اشارة الاقتران, المتباينات, متعدد القاعدة, القيمة المطلقة, اكبر عدد صحيح, الأسس واللوغاريتمات, الاقتران الأسي, الاقتران اللوغاريتمي )
    const questionsData = [
        // الدرس الأول: الاقتران الزوجي والاقتران الفردي
        {
            id: 1,
            lesson: "الدرس الأول: الاقتران الزوجي والاقتران الفردي",
            question: "أي من الاقترانات الآتية يُعتبر اقتراناً زوجياً؟",
            options: [
                "ق(س) = س³",
                "ق(س) = س² + ٤",
                "ق(س) = س³ + س",
                "ق(س) = س + ١"
            ],
            answer: 1
        },
        {
            id: 2,
            lesson: "الدرس الأول: الاقتران الزوجي والاقتران الفردي",
            question: "إذا كان ق(س) اقتراناً فردياً وكان ق(٣) = ٥ ، فإن قيمة ق(-٣) تساوي:",
            options: [
                "٥",
                "-٥",
                "١/٥",
                "٠"
            ],
            answer: 1
        },
        // الدرس الثاني: تمثيل الاقترانات باستخدام الانسحاب
        {
            id: 3,
            lesson: "الدرس الثاني: تمثيل الاقترانات باستخدام الانسحاب",
            question: "منحنى الاقتران هـ(س) = (س - ٢)² هو انسحاب لمنحنى ق(س) = س² بمقدار وحدتين إلى:",
            options: [
                "الأعلى",
                "الأسفل",
                "اليمين",
                "اليسار"
            ],
            answer: 2
        },
        {
            id: 4,
            lesson: "الدرس الثاني: تمثيل الاقترانات باستخدام الانسحاب",
            question: "معادلة منحنى الاقتران الناتج عن إزاحة منحنى ق(س) = |س| بمقدار ٣ وحدات إلى الأسفل هي:",
            options: [
                "هـ(س) = |س - ٣|",
                "هـ(س) = |س + ٣|",
                "هـ(س) = |س| - ٣",
                "هـ(س) = |س| + ٣"
            ],
            answer: 2
        },
        // الدرس الثالث: تمثيل الاقترانات باستخدام الانعكاس
        {
            id: 5,
            lesson: "الدرس الثالث: تمثيل الاقترانات باستخدام الانعكاس",
            question: "منحنى الاقتران هـ(س) = -س² هو انعكاس لمنحنى ق(س) = س² في محور:",
            options: [
                "السينات",
                "الصادات",
                "مستقيم س = ص",
                "نقطة الأصل"
            ],
            answer: 0
        },
        {
            id: 6,
            lesson: "الدرس الثالث: تمثيل الاقترانات باستخدام الانعكاس",
            question: "إذا تم انعكاس منحنى الاقتران ق(س) = جذر(س) حول محور الصادات، فإن قاعدة الاقتران الجديد هـ(س) هي:",
            options: [
                "هـ(س) = - جذر(س)",
                "هـ(س) = جذر(-س)",
                "هـ(س) = 1 / جذر(س)",
                "هـ(س) = - جذر(-س)"
            ],
            answer: 1
        },
        // الدرس الرابع: إشارة الاقتران
        {
            id: 7,
            lesson: "الدرس الرابع: إشارة الاقتران",
            question: "إشارة الاقتران الخطي ق(س) = ٢س - ٦ تكون موجبة عندما:",
            options: [
                "س < ٣",
                "س > ٣",
                "س < -٣",
                "س > -٣"
            ],
            answer: 1
        },
        {
            id: 8,
            lesson: "الدرس الرابع: إشارة الاقتران",
            question: "صفر الاقتران ق(س) = ٩ - س² هما س = ٣ و س = -٣. تكون إشارة الاقتران سالبة في الفترة:",
            options: [
                "(-٣ ، ٣)",
                "[-٣ ، ٣]",
                "(-أنهائية ، -٣) U (٣ ، أنهائية)",
                "[-٣ ، أنهائية)"
            ],
            answer: 2
        },
        // الدرس الخامس: حل المتباينات
        {
            id: 9,
            lesson: "الدرس الخامس: حل المتباينات",
            question: "مجموعة حل المتباينة س² - ٤ <= ٠ هي الفترة:",
            options: [
                "(-أنهائية ، -٢]",
                "[٢ ، أنهائية)",
                "[-٢ ، ٢]",
                "(-٢ ، ٢)"
            ],
            answer: 2
        },
        {
            id: 10,
            lesson: "الدرس الخامس: حل المتباينات",
            question: "مجموعة حل المتباينة |س - ١| < ٣ هي الفترة:",
            options: [
                "(-٢ ، ٤)",
                "[-٢ ، ٤]",
                "(-أنهائية ، -٢)",
                "(٤ ، أنهائية)"
            ],
            answer: 0
        },
        // الدرس السادس: الاقترانات متعددة القاعدة
        {
            id: 11,
            lesson: "الدرس السادس: الاقترانات متعددة القاعدة",
            question: "إذا كان ق(س) = { س² عندما س >= ١ ،  ٣س عندما س < ١ } ، فإن قيمة ق(-٢) تساوي:",
            options: [
                "٤",
                "-٦",
                "٦",
                "-٤"
            ],
            answer: 1
        },
        {
            id: 12,
            lesson: "الدرس السادس: الاقترانات متعددة القاعدة",
            question: "إذا كان ق(س) = { ٢س + ١ عندما س > ٠ ،  ٥ عندما س <= ٠ } ، فإن قيمة ق(٠) تساوي:",
            options: [
                "١",
                "٠",
                "٥",
                "غير معرفة"
            ],
            answer: 2
        },
        // الدرس السابع: اقتران القيمة المطلقة
        {
            id: 13,
            lesson: "الدرس السابع: اقتران القيمة المطلقة",
            question: "إعادة تعريف الاقتران ق(س) = |س - ٥| عندما س < ٥ هي:",
            options: [
                "س - ٥",
                "٥ - س",
                "س + ٥",
                "-س - ٥"
            ],
            answer: 1
        },
        {
            id: 14,
            lesson: "الدرس السابع: اقتران القيمة المطلقة",
            question: "مجموعة حل المعادلة |٢س - ٤| = ٦ هي:",
            options: [
                "{٥}",
                "{-١}",
                "{٥ ، -١}",
                "{٥ ، ١}"
            ],
            answer: 2
        },
        // الدرس الثامن: اقتران أكبر عدد صحيح
        {
            id: 15,
            lesson: "الدرس الثامن: اقتران أكبر عدد صحيح",
            question: "قيمة [ ٣.٧ ] (أكبر عدد صحيح للعدد ٣.٧) تساوي:",
            options: [
                "٣",
                "٤",
                "٣.٥",
                "٠"
            ],
            answer: 0
        },
        {
            id: 16,
            lesson: "الدرس الثامن: اقتران أكبر عدد صحيح",
            question: "قيمة [ -٢.٣ ] تساوي:",
            options: [
                "-٢",
                "-٣",
                "٢",
                "٣"
            ],
            answer: 1
        },
        {
            id: 17,
            lesson: "الدرس الثامن: اقتران أكبر عدد صحيح",
            question: "طول الدرجة للاقتران ق(س) = [ ٠.٥ س + ١ ] يساوي:",
            options: [
                "٠.٥",
                "١",
                "٢",
                "٤"
            ],
            answer: 2
        },
        // الدرس الأول (الوحدة الثانية): الأسس واللوغاريتمات
        {
            id: 18,
            lesson: "الدرس الأول: الأسس واللوغاريتمات",
            question: "الصورة المقابلة للجملة الأسية ٢⁵ = ٣٢ بالصورة اللوغاريتمية هي:",
            options: [
                "لو₂ (٣٢) = ٥",
                "لو₅ (٣٢) = ٢",
                "لو₃٢ (٢) = ٥",
                "لو₂ (٥) = ٣٢"
            ],
            answer: 0
        },
        {
            id: 19,
            lesson: "الدرس الأول: الأسس واللوغاريتمات",
            question: "قيمة المقدار اللوغاريتمي: لو₃ (٨١) تساوي:",
            options: [
                "٣",
                "٤",
                "٩",
                "٢٧"
            ],
            answer: 1
        },
        {
            id: 20,
            lesson: "الدرس الأول: الأسس واللوغاريتمات",
            question: "إذا كان لو₅ (س) = ٣ ، فإن قيمة س تساوي:",
            options: [
                "١٥",
                "٨",
                "١٢٥",
                "٢٤٣"
            ],
            answer: 2
        },
        // الدرس الثاني (الوحدة الثانية): الاقتران الأسي
        {
            id: 21,
            lesson: "الدرس الثاني: الاقتران الأسي",
            question: "الاقتران الأسي ق(س) = (٣)^س يمر بالنقطة:",
            options: [
                "(٠ ، ٠)",
                "(٠ ، ١)",
                "(١ ، ٠)",
                "(٣ ، ٠)"
            ],
            answer: 1
        },
        {
            id: 22,
            lesson: "الدرس الثاني: الاقتران الأسي",
            question: "إذا كان (٢)^(س - ١) = ٨ ، فإن قيمة س تساوي:",
            options: [
                "٣",
                "٤",
                "٢",
                "٥"
            ],
            answer: 1
        },
        // الدرس الثالث (الوحدة الثانية): الاقتران اللوغاريتمي
        {
            id: 23,
            lesson: "الدرس الثالث: الاقتران اللوغاريتمي",
            question: "مجال الاقتران اللوغاريتمي ق(س) = لو₂ (س - ٣) هو الفترة:",
            options: [
                "[٣ ، أنهائية)",
                "(٣ ، أنهائية)",
                "(-أنهائية ، ٣)",
                "ح"
            ],
            answer: 1
        },
        {
            id: 24,
            lesson: "الدرس الثالث: الاقتران اللوغاريتمي",
            question: "المقطع السيني لمنحنى الاقتران ق(س) = لو₄ (س) هو:",
            options: [
                "س = ٠",
                "س = ١",
                "س = ٤",
                "لا يوجد مقطع سيني"
            ],
            answer: 1
        },
        {
            id: 25,
            lesson: "الدرس الثالث: الاقتران اللوغاريتمي",
            question: "المقدار اللوغاريتمي لو(أ*ب) يكافئ:",
            options: [
                "لو(أ) * لو(ب)",
                "لو(أ) + لو(ب)",
                "لو(أ) - لو(ب)",
                "لو(أ) / لو(ب)"
            ],
            answer: 1
        }
    ];

    // Render Questions
    function renderQuestions() {
        const container = document.getElementById('questions-container');
        const optionsPrefix = ['أ', 'ب', 'جـ', 'د'];

        questionsData.forEach((q, index) => {
            const card = document.createElement('div');
            card.className = 'question-card';
            card.id = `q-card-${index}`;

            let optionsHtml = '';
            q.options.forEach((opt, optIdx) => {
                optionsHtml += `
                    <li class="option-item">
                        <label class="option-label" id="label-q${index}-opt${optIdx}">
                            <input type="radio" name="question_${index}" value="${optIdx}">
                            <span><strong>(${optionsPrefix[optIdx]})</strong> <span class="math-text">${opt}</span></span>
                        </label>
                    </li>
                `;
            });

            card.innerHTML = `
                <div class="question-title">
                    <span style="color:var(--primary-color);">السؤال ${index + 1}:</span> ${q.question}
                </div>
                <ul class="options-list">
                    ${optionsHtml}
                </ul>
                <div class="feedback-box" id="feedback-q${index}"></div>
            `;

            container.appendChild(card);
        });
    }

    // Submit Quiz Function
    function submitQuiz(e) {
        e.preventDefault();

        const nameInput = document.getElementById('studentName');
        const classInput = document.getElementById('studentClass');
        const nameError = document.getElementById('nameError');
        const classError = document.getElementById('classError');

        let isValid = true;

        if (!nameInput.value.trim()) {
            nameError.style.display = 'block';
            isValid = false;
        } else {
            nameError.style.display = 'none';
        }

        if (!classInput.value) {
            classError.style.display = 'block';
            isValid = false;
        } else {
            classError.style.display = 'none';
        }

        if (!isValid) return;

        // Calculate Score
        let score = 0;
        const totalQuestions = questionsData.length;
        const studentAnswers = [];

        questionsData.forEach((q, index) => {
            const selectedOption = document.querySelector(`input[name="question_${index}"]:checked`);
            const feedbackBox = document.getElementById(`feedback-q${index}`);
            const optionsPrefix = ['أ', 'ب', 'جـ', 'د'];
            
            let selectedVal = null;
            if (selectedOption) {
                selectedVal = parseInt(selectedOption.value);
                studentAnswers.push(selectedVal);
            } else {
                studentAnswers.push(null);
            }

            // Lock input after submit
            const radios = document.querySelectorAll(`input[name="question_${index}"]`);
            radios.forEach(r => r.disabled = true);

            const correctIdx = q.answer;
            const correctLabel = document.getElementById(`label-q${index}-opt${correctIdx}`);

            if (selectedVal !== null) {
                const selectedLabel = document.getElementById(`label-q${index}-opt${selectedVal}`);
                if (selectedVal === correctIdx) {
                    score++;
                    selectedLabel.classList.add('selected-correct');
                    feedbackBox.className = 'feedback-box correct-answer-text';
                    feedbackBox.innerHTML = `إجابة صحيحة! أحسنت.`;
                } else {
                    selectedLabel.classList.add('selected-wrong');
                    correctLabel.classList.add('highlight-correct');
                    feedbackBox.className = 'feedback-box wrong-answer-text';
                    feedbackBox.innerHTML = `إجابة خاطئة. الإجابة الصحيحة هي: (${optionsPrefix[correctIdx]}) ${q.options[correctIdx]}`;
                }
            } else {
                correctLabel.classList.add('highlight-correct');
                feedbackBox.className = 'feedback-box wrong-answer-text';
                feedbackBox.innerHTML = `لم تقم بالإجابة عن هذا السؤال. الإجابة الصحيحة هي: (${optionsPrefix[correctIdx]}) ${q.options[correctIdx]}`;
            }

            feedbackBox.style.display = 'block';
        });

        // Save Data in LocalStorage
        const submissionData = {
            studentName: nameInput.value.trim(),
            studentClass: classInput.value,
            score: score,
            total: totalQuestions,
            percentage: Math.round((score / totalQuestions) * 100),
            date: new Date().toLocaleString('ar-EG'),
            answers: studentAnswers
        };

        // Save submissions array to localStorage
        let submissions = JSON.parse(localStorage.getItem('quiz_submissions') || '[]');
        submissions.push(submissionData);
        localStorage.setItem('quiz_submissions', JSON.stringify(submissions));

        // Display Summary Result
        const resultSection = document.getElementById('result-section');
        const scoreText = document.getElementById('scoreText');
        const feedbackText = document.getElementById('feedbackText');

        scoreText.innerHTML = `النتيجة: ${score} من ${totalQuestions} (${submissionData.percentage}%)`;
        
        if (submissionData.percentage >= 85) {
            feedbackText.innerHTML = `ممتاز جداً يا ${submissionData.studentName}! لديك مستوًى رائع وخلفية قوية في المادة.`;
        } else if (submissionData.percentage >= 65) {
            feedbackText.innerHTML = `أحسنت يا ${submissionData.studentName}! أداؤك جيد جداً، مع الحاجة لمراجعة بعض المفاهيم.`;
        } else if (submissionData.percentage >= 50) {
            feedbackText.innerHTML = `أداء مقبول يا ${submissionData.studentName}. ننصح بمراجعة الدروس السابقة لتعزيز فهمك.`;
        } else {
            feedbackText.innerHTML = `عزيزي الطالب ${submissionData.studentName}، يرجى مراجعة المواضيع والمفاهيم الأساسية قبل البدء في المنهاج.`;
        }

        resultSection.style.display = 'block';
        document.getElementById('submitBtn').disabled = true;
        document.getElementById('submitBtn').style.backgroundColor = '#ccc';
        document.getElementById('submitBtn').innerText = 'تم تسليم الاختبار وحفظ النتائج';

        // Scroll to results
        resultSection.scrollIntoView({ behavior: 'smooth' });
    }

    // Initialize page
    window.onload = function() {
        renderQuestions();
    };
</script>

</body>
</html>
'''

with open('diagnostic_test.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML File successfully created: diagnostic_test.html")