package org.codecop;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;

/**
 * Counts words of a text and provides basic analysis of that.
 */
public class WordCounter {

    private final List<String> words;

    public WordCounter(String sentence) {
        words = Arrays.asList(sentence.split("\\s+"));
    }

    /**
     * Load words from a text file.
     */
    public WordCounter(File wordFile) throws IOException {
        this(StringToFile.read(wordFile));
    }

    public int numberOfWords() {
        return words.size();
    }

    /**
     * @return unique words sorted alphabetically.
     */
    public String[] uniqueWords() {
        List<String> uniqueWords = new ArrayList<String>(new HashSet<String>(words));
        Collections.sort(uniqueWords);
        return uniqueWords.toArray(new String[uniqueWords.size()]);
    }

    public boolean containsWord(String word) {
        return words.contains(word);
    }

    public Integer countOf(String word) {
        int sum = 0;
        for (String s : words) {
            if (word.equals(s)) {
                sum++;
            }
        }

        if (sum > 0) {
            return sum;
        }
        return null;
    }

    /**
     * @return ratio of this word's occurance against all words.
     */
    public double ratioOf(String word) {
        Integer count = countOf(word);
        if (count == null) {
            throw new IllegalArgumentException(word + " not in sentence");
        }
        return 1.0 * count / numberOfWords();
    }

}
